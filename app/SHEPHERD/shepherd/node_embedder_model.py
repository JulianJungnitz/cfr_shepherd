# Pytorch 
import torch
import torch.nn as nn

import torch.nn.functional as F
from torch_geometric.nn import BatchNorm, LayerNorm, GATv2Conv
from torch_geometric.loader.neighbor_loader import NeighborLoader

# Pytorch Lightning
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger

# General
import numpy as np
import math
import tqdm
import time
import wandb

# Own
from utils.pretrain_utils import sample_node_for_et, get_batched_data, get_edges, calc_metrics, plot_roc_curve, metrics_per_rel
from decoders import bilinear, trans, dot

# Global variables
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class NodeEmbeder(pl.LightningModule):

    def __init__(self, all_data, edge_attr_dict, hp_dict=None, num_nodes=None, combined_training=False, spl_mat=[], ):
        print("NodeEmbeder: __init__")
        super().__init__()

        # save hyperparameters
        self.save_hyperparameters("hp_dict", ignore=["spl_mat"])

        # Data
        self.all_data = all_data
        self.edge_attr_dict = edge_attr_dict

        print("Size of all_data: ", len(all_data))
        print("Size of edge_attr_dict: ", len(edge_attr_dict))

        # Model parameters
        self.lr = self.hparams.hp_dict['lr']
        self.lr_factor = self.hparams.hp_dict['lr_factor']
        self.lr_patience = self.hparams.hp_dict['lr_patience']
        self.lr_threshold = self.hparams.hp_dict['lr_threshold']
        self.lr_threshold_mode = self.hparams.hp_dict['lr_threshold_mode']
        self.lr_cooldown = self.hparams.hp_dict['lr_cooldown']
        self.min_lr = self.hparams.hp_dict['min_lr']
        self.eps = self.hparams.hp_dict['eps']
        
        self.wd = self.hparams.hp_dict['wd']
        self.decoder_type = self.hparams.hp_dict['decoder_type']
        self.pred_threshold = self.hparams.hp_dict['pred_threshold']
        
        self.use_spl = None
        self.spl_mat = []
        self.spl_dim = 0
        
        self.nfeat = self.hparams.hp_dict['nfeat']
        self.nhid1 = self.hparams.hp_dict['hidden'] * 2
        self.nhid2 = self.hparams.hp_dict['hidden']
        self.output = self.hparams.hp_dict['output']
        
        print("Number of Nodes: ", num_nodes)
        self.node_emb = nn.Embedding(num_nodes, self.nfeat)
        print("Embeddings initialized")
        
        self.num_nodes = num_nodes 
        self.num_relations = len(edge_attr_dict)
        self.n_heads = self.hparams.hp_dict['n_heads']
        self.dropout = self.hparams.hp_dict['dropout']
        self.norm_method = self.hparams.hp_dict['norm_method']

        # Select decoder
        if self.decoder_type == "bilinear": self.decoder = bilinear
        elif self.decoder_type == "trans": self.decoder = trans
        elif self.decoder_type == "dot": self.decoder = dot
        
        self.n_layers = 3
        
        self.loss_type = self.hparams.hp_dict['loss']
        self.combined_training = combined_training

        # Conv layers
        self.convs = torch.nn.ModuleList()
        self.convs.append(GATv2Conv(self.nfeat, self.nhid1, self.n_heads)) # input = nfeat, output = nhid1*n_heads
        if self.n_layers == 3:
            self.convs.append(GATv2Conv(self.nhid1*self.n_heads, self.nhid2, self.n_heads)) # input = nhid1*n_heads, output = nhid2*n_heads
            self.convs.append(GATv2Conv(self.nhid2*self.n_heads, self.output, self.n_heads)) # input = nhid2*n_heads, output = output*n_heads
        else:
            self.convs.append(GATv2Conv(self.nhid1*self.n_heads, self.output, self.n_heads)) # input = nhid2*n_heads, output = output*n_heads
        
        # Relation learnable weights
        self.relation_weights = nn.Parameter(torch.Tensor(self.num_relations, self.output * self.n_heads))

        # Normalization (applied after a single conv layer)

        fix_layer_size = False # If True, the layer size is fixed to 1
        print("Sizes: ", self.nhid1*self.n_heads, self.nhid2*self.n_heads, "Fix Layer Size: ", fix_layer_size)

        if self.norm_method == "batch":
            self.norms = torch.nn.ModuleList()
            self.norms.append(BatchNorm(self.nhid1*self.n_heads if not fix_layer_size else 1))
            self.norms.append(BatchNorm(self.nhid2*self.n_heads if not fix_layer_size else 1))
        elif self.norm_method == "layer":
            self.norms = torch.nn.ModuleList()
            self.norms.append(LayerNorm(self.nhid1*self.n_heads if not fix_layer_size else 1))
            self.norms.append(LayerNorm(self.nhid2*self.n_heads if not fix_layer_size else 1))
        elif self.norm_method == "batch_layer":
            self.batch_norms = torch.nn.ModuleList()
            self.batch_norms.append(BatchNorm(self.nhid1*self.n_heads if not fix_layer_size else 1))
            if self.n_layers == 3: self.batch_norms.append(BatchNorm(self.nhid2*self.n_heads if not fix_layer_size else 1))
            self.layer_norms = torch.nn.ModuleList()
            self.layer_norms.append(LayerNorm(self.nhid1*self.n_heads if not fix_layer_size else 1))
            if self.n_layers == 3: self.layer_norms.append(LayerNorm(self.nhid2*self.n_heads if not fix_layer_size else 1))

        self.reset_parameters()

    def reset_parameters(self):
        for conv in self.convs:
            conv.reset_parameters()
        nn.init.xavier_uniform_(self.relation_weights, gain = nn.init.calculate_gain('leaky_relu'))

    def forward(self, n_ids, adjs): 
        x = self.node_emb(n_ids)
        
        gat_attn = []
        assert len(adjs) == self.n_layers
        for i, (edge_index, _, edge_type, size) in enumerate(adjs):
            
            # Update node embeddings
            x_target = x[:size[1]]  # Target nodes are always placed first. 
            
            # print("Type: ", type(edge_index))
            # print("Edge Index size: ", edge_index.size)
            # print("Edge Index (E_i) size: ", edge_index.edge_index.size())

            x, (edge_i, alpha) = self.convs[i]((x, x_target), edge_index, return_attention_weights=True)

            edge_i = edge_i.detach().cpu()
            alpha = alpha.detach().cpu()
            edge_i[0,:] = n_ids[edge_i[0,:]]
            edge_i[1,:] = n_ids[edge_i[1,:]]
            gat_attn.append((edge_i, alpha))

            # Normalize
            if i != self.n_layers - 1:
                if self.norm_method in ["batch", "layer"]:
                    x = self.norms[i](x)
                elif self.norm_method == "batch_layer":
                    x = self.layer_norms[i](x)
                x = F.leaky_relu(x)
                if self.norm_method == "batch_layer":
                    x = self.batch_norms[i](x)
                x = F.dropout(x, p=self.dropout, training=self.training)

        return x, gat_attn



    
    def get_negative_target_nodes(self, data, pos_target_embeds, curr_pos_target_embeds, all_edge_types):
        if self.hparams.hp_dict['negative_sampler_approach'] == 'all':
            # get negative targets by shuffling positive targets
            if 'index_to_node_features_pos' in data:
                rand_index = torch.randperm(data.index_to_node_features_pos.size(0))
            else:
                rand_index = torch.randperm(curr_pos_target_embeds.size(0))
            
        elif self.hparams.hp_dict['negative_sampler_approach'] == 'by_edge_type':
            # get negative targets by shuffling positive targets within each edge type
            et_ids, et_counts = all_edge_types.unique(return_counts=True)
            targets_dict = self.create_target_dict(all_edge_types, et_ids) # indices into all_edge_types for each edge type
            # print("Move to GPU: negative sampling")
            
            # rand_index = torch.tensor(np.vectorize(sample_node_for_et)(all_edge_types.cpu(), targets_dict)).to(device)
            if all_edge_types.numel() == 0:
                print("No edge types found")
                rand_index = torch.tensor([], device=device, )
            else:
                rand_indices = []
                for et in all_edge_types.cpu().numpy():
                    rand_indices.append(sample_node_for_et(et, targets_dict))

                rand_index = torch.tensor(rand_indices, device=device,)


            # print("Moved: negative sampling")

        if 'index_to_node_features_pos' in data:
            index_to_node_features_neg = data.index_to_node_features_pos[rand_index] #NOTE: currently possible to get the same node as positive & negative target
            curr_neg_target_embeds = pos_target_embeds[index_to_node_features_neg,:]
        else:
            curr_neg_target_embeds = curr_pos_target_embeds[rand_index,:]
        
        return curr_neg_target_embeds

    def create_target_dict(self, all_edge_types, et_ids):
        targets_dict = {}
        for k in et_ids:
            indices = (all_edge_types == int(k)).nonzero().cpu()
            targets_dict[int(k)] = indices
        return targets_dict

    def decode(self, data, source_embeds, pos_target_embeds, all_edge_types): 
        curr_source_embeds = source_embeds[data.index_to_node_features_pos,:]
        curr_pos_target_embeds = pos_target_embeds[data.index_to_node_features_pos,:]

        ts = time.time()
        curr_neg_target_embeds = self.get_negative_target_nodes(data, pos_target_embeds, curr_pos_target_embeds, all_edge_types)
        te = time.time()
        if self.hparams.hp_dict['time']:
            print(f"Negative sampling took {te - ts:0.4f} seconds")

        # Get source & targets for pos & negative edges
        source = torch.cat([curr_source_embeds, curr_source_embeds])
        target = torch.cat([curr_pos_target_embeds, curr_neg_target_embeds])
        all_edge_types = torch.cat([all_edge_types, all_edge_types])
        data.all_edge_types = all_edge_types

        if self.decoder_type == "dot": 
            return data, self.decoder(source, target)
        else: 
            relation = self.relation_weights[all_edge_types]
            return data, self.decoder(source, relation, target)

    def get_predictions(self, data, embed):
        
        # Apply decoder
        source_embed, target_embed = embed.split(embed.size(0) // 2, dim=0)
        data, raw_pred = self.decode(data, source_embed, target_embed, data.pos_edge_types)
        
        # Apply activation
        if self.loss_type != "max-margin": 
            pred = torch.sigmoid(raw_pred)
        else: 
            pred = torch.tanh(raw_pred)
        
        return data, raw_pred, pred

    def get_link_labels(self, edge_types):
        num_links = edge_types.size(0) 
        link_labels = torch.zeros(num_links, dtype=torch.float, device=edge_types.device)
        link_labels[:(int(num_links/2))] = 1.
        link_labels[(int(num_links/2)):] = 0.
        return link_labels

    def _step(self, data, dataset_type):

        if not self.combined_training: 
            ts = time.time()
            # print("try access all_data")
            data = get_batched_data(data, self.all_data) 
            # print("accessed all_data")
            tm = time.time()
            data = get_edges(data, self.all_data, dataset_type)
            te=time.time()
        # print("Move to GPU: _step - data")
        data = data.to(device)
        # print("Moved: _step - data")

        # Get predictions
        t0 = time.time()
        out, gat_attn = self.forward(data.n_id, data.adjs) 
        t1 = time.time()
        data, raw_pred, pred = self.get_predictions(data, out)
        t2 = time.time()

        # Calculate loss
        link_labels = self.get_link_labels(data.all_edge_types)
        loss = self.calc_loss(pred, link_labels)
        t3 = time.time()

        # Calculate metrics
        if self.loss_type == "max-margin":
            metric_pred = torch.sigmoid(raw_pred)
            self.logger.experiment.log({f'{dataset_type}/node_predicted_probs': wandb.Histogram(metric_pred.cpu().detach().numpy())})
        else: metric_pred = pred
        roc_score, ap_score, acc, f1 = calc_metrics(metric_pred.cpu().detach().numpy(), link_labels.cpu().detach().numpy(), self.pred_threshold)
        self.logger.experiment.log({f'{dataset_type}/node_roc_curve': plot_roc_curve(metric_pred.cpu().detach().numpy(), link_labels.cpu().detach().numpy())})
        
        t4 = time.time()
        if self.hparams.hp_dict['time']:
            print(f'It took {tm-ts:0.2f}s to get batched data, {te-tm:0.2f}s to get edges, {t1-t0:0.2f}s to complete forward pass, {t2-t1:0.2f}s to decode, {t3-t2:0.2f}s to calc loss, and {t4-t3:0.2f}s to calc other metrics.')

        return data, loss, pred, link_labels, roc_score, ap_score, acc, f1

    def training_step(self, data, data_idx):
        data, loss, pred, link_labels, roc_score, ap_score, acc, f1 = self._step(data, 'train')
        
        logs = {"train/node_batch_loss": loss.detach(), 
                "train/node_roc": roc_score, 
                "train/node_ap": ap_score, 
                "train/node_acc": acc, 
                "train/node_f1": f1
               }

        rel_logs = metrics_per_rel(pred, link_labels, self.edge_attr_dict, data.all_edge_types, "train", self.pred_threshold)
        logs.update(rel_logs)
        self._logger(logs)
        return {'loss': loss, 'logs': logs}

    def on_train_epoch_end(self, ):     
        roc_train = []
        ap_train = []
        acc_train = []
        f1_train = []
        total_train_loss = []
        outputs = self.trainer.callback_metrics

        roc_train.append(outputs["train/node_roc"].cpu().item())
        ap_train.append(outputs["train/node_ap"].cpu().item())
        acc_train.append(outputs["train/node_acc"].cpu().item())
        f1_train.append(outputs["train/node_f1"].cpu().item())
        total_train_loss.append(outputs["train/node_batch_loss"].cpu().item())

        self._logger({"train/node_total_loss": torch.mean(torch.Tensor(total_train_loss)), 
                      "train/node_total_roc": np.mean(roc_train), 
                      "train/node_total_ap": np.mean(ap_train), 
                      "train/node_total_acc": np.mean(acc_train), 
                      "train/node_total_f1": np.mean(f1_train)})
        self._logger({'node_curr_epoch': self.current_epoch})

    def validation_step(self, data, data_idx):
        data, loss, pred, link_labels, roc_score, ap_score, acc, f1 = self._step(data, 'val')
        
        logs = {"val/node_batch_loss": loss.detach().cpu(), 
                "val/node_roc": roc_score, 
                "val/node_ap": ap_score, 
                "val/node_acc": acc, 
                "val/node_f1": f1
               }

        rel_logs = metrics_per_rel(pred, link_labels, self.edge_attr_dict, data.all_edge_types, "val", self.pred_threshold)
        logs.update(rel_logs)
        self._logger(logs)
        return logs

    def on_validation_epoch_end(self,):
        roc_val = []
        ap_val = []
        acc_val = []
        f1_val = []
        total_val_loss = []
        # print("on_validation_epoch")
        # print("Trainer Callback Metrics: ", self.trainer.callback_metrics)
        # print("------------------------------------")

        
        
        roc_val.append(self.trainer.callback_metrics["val/node_roc"].cpu().item())
        ap_val.append(self.trainer.callback_metrics["val/node_ap"].cpu().item())
        acc_val.append(self.trainer.callback_metrics["val/node_acc"].cpu().item())
        f1_val.append(self.trainer.callback_metrics["val/node_f1"].cpu().item())
        total_val_loss.append(self.trainer.callback_metrics["val/node_batch_loss"].cpu().item())
        
        self._logger({"val/node_total_loss": torch.mean(torch.Tensor(total_val_loss)), 
                      "val/node_total_roc": np.mean(roc_val), 
                      "val/node_total_ap": np.mean(ap_val), 
                      "val/node_total_acc": np.mean(acc_val), 
                      "val/node_total_f1": np.mean(f1_val)})
        self._logger({'node_curr_epoch': self.current_epoch})

    def test_step(self, data, data_idx):
        data, loss, pred, link_labels, roc_score, ap_score, acc, f1 = self._step(data, 'test')

        logs = {"test/node_batch_loss": loss.detach().cpu(), 
                "test/node_roc": roc_score, 
                "test/node_ap": ap_score, 
                "test/node_acc": acc, 
                "test/node_f1": f1
               }

        rel_logs = metrics_per_rel(pred, link_labels, self.edge_attr_dict, data.all_edge_types, "test", self.pred_threshold)
        logs.update(rel_logs)
        self._logger(logs)
        return logs

    def on_test_epoch_end(self, ):
        roc = []
        ap = []
        acc = []
        f1 = []

        outputs = self.trainer.callback_metrics
        roc.append(outputs["test/node_roc"].cpu().item())
        ap.append(outputs["test/node_ap"].cpu().item())
        acc.append(outputs["test/node_acc"].cpu().item())
        f1.append(outputs["test/node_f1"].cpu().item())
        
        self._logger({"test/node_total_roc": np.mean(roc), 
                      "test/node_total_ap": np.mean(ap), 
                      "test/node_total_acc": np.mean(acc), 
                      "test/node_total_f1": np.mean(f1)})
        self._logger({'node_curr_epoch': self.current_epoch})

    
    def predict(self, data, unique_n_ids):

        print("DATA: ", data)
        # DATA:  Data(edge_index=[2, 73435672], edge_attr=[73435672], train_mask=[73435672], val_mask=[73435672], test_mask=[73435672])

        # print("BATCH: ", batch)
        # BATCH:  Data(adjs=[3], batch_size=23734, patient_ids=[10], n_id=[232076], disease_one_hot_labels=[10, 1169], phenotype_names=[10], cand_gene_names=[10], corr_gene_names=[10], disease_names=[10], cand_disease_names=[10], batch_pheno_nid=[10, 25], batch_corr_gene_nid=[10, 0], batch_disease_nid=[10, 1], batch_cand_disease_nid=[10, 1169])
        # e_emb.weight.shape[0], device=self.device)
        
        # return self.forward(batch.n_id, batch.adjs)

        # batch_n_id = batch.n_id.to(self.device)  # Move to the correct device if necessary
        # print(f"batch_n_id: {batch_n_id.shape}")

        n_id = torch.arange(self.node_emb.weight.shape[0], device=self.device)
        x = self.node_emb(unique_n_ids)
        print(f"Initial embeddings shape: {x.shape}")

        # batch_edge_index = batch.edge_index.to(self.device)

        # forward(x, batch_edge_index, return_attention_weights=False)

        gat_attn = []
        for i in range(len(self.convs)):
            # Update node embeddings
            print(f"Move to GPU: predict - update node embeddings at layer {i}")
            x = self.convs[i](x, data.edge_index.to(self.device),)
            print(f"Moved: predict - update node embeddings at layer {i}")

            # Normalize
            if i != self.n_layers - 1:
                if self.norm_method in ["batch", "layer"]:
                    if self.norm_method == "batch" and len(self.batch_norms) > i:
                        x = self.batch_norms[i](x)
                        print(f"Applied batch norm at layer {i}")
                    elif self.norm_method == "layer" and len(self.layer_norms) > i:
                        x = self.layer_norms[i](x)
                        print(f"Applied layer norm at layer {i}")
                elif self.norm_method == "batch_layer":
                    if len(self.layer_norms) > i and len(self.batch_norms) > i:
                        x = self.layer_norms[i](x)
                        x = F.leaky_relu(x)
                        x = self.batch_norms[i](x)
                        print(f"Applied batch_layer norm at layer {i}")
                    else:
                        x = F.leaky_relu(x)
                        print(f"Applied leaky_relu at layer {i} without normalization")

            # Activation
            x = F.leaky_relu(x)
            print(f"Applied leaky_relu at layer {i}")

        return x, gat_attn

    def predict_step(self, data, data_idx):
        x, gat_attn = self.predict(data)
        return x, gat_attn
    
    
    

    def predict_in_batches(self, data,  node_idx=None):
        batch_size=10
        """
        Compute embeddings for all nodes by sampling neighbors in small batches.
        """
        self.eval()  # inference mode
        device = self.device
        
        x_all = torch.zeros(self.num_nodes, self.output * self.n_heads,
                            device='cpu')

        
        loader = NeighborLoader(
            data,
            num_neighbors=[15, 10, 5],  
            batch_size=batch_size,
            shuffle=False,
            input_nodes=node_idx,           
            num_workers=4,               
        )

        with torch.no_grad():
            for sub_data in loader:
                batch_size = sub_data.batch_size
                n_id = sub_data.n_id
                out = self.forward(n_id, sub_data)
                x_all[n_id.cpu()] = out.cpu()

        return x_all
    

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr, weight_decay = self.wd)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=self.lr_factor, patience=self.lr_patience, threshold=self.lr_threshold, threshold_mode=self.lr_threshold_mode, cooldown=self.lr_cooldown, min_lr=self.min_lr, eps=self.eps)
        return {
                "optimizer": optimizer,
                "lr_scheduler": 
                    {
                    "scheduler": scheduler,
                    "monitor": "val/node_total_loss",
                    'name': 'curr_lr'
                    },
                }

    def _logger(self, logs):
        for k, v in logs.items():
            self.log(k, v)

    def calc_loss(self, pred, y):
        if self.loss_type == "BCE":
            loss = F.binary_cross_entropy(pred, y, reduction='none')
            norm_loss = torch.mean(loss)

        elif self.loss_type == "max-margin": 
            loss = ((1 - (pred[y == 1] - pred[y != 1])).clamp(min=0).mean())
            norm_loss = loss

        return norm_loss 

