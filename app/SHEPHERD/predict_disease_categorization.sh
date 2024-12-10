
cd app/SHEPHERD/shepherd

patient_aggr_nodes=$1


python predict.py \
    --run_type disease_characterization \
    --patient_data my_data \
    --edgelist KG_edgelist_mask.txt \
    --node_map KG_node_map.txt \
    --saved_node_embeddings_path checkpoints/pretrain.ckpt \
    --best_ckpt checkpoints/patient_NCA/best/best.ckpt \
    --patient_aggr_nodes $patient_aggr_nodes
