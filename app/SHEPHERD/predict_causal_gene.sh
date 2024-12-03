
cd app/SHEPHERD/shepherd



python predict.py \
    --run_type causal_gene_discovery \
    --patient_data my_data \
    --edgelist KG_edgelist_mask.txt \
    --node_map KG_node_map.txt \
    --saved_node_embeddings_path checkpoints/pretrain.ckpt \
    --best_ckpt checkpoints/causal_gene_discovery.ckpt
