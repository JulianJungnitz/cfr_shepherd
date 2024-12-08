pwd
cd app/SHEPHERD/shepherd

patient_aggr_nodes=$1


python predict.py \
    --run_type patients_like_me \
    --patient_data my_data \
    --edgelist KG_edgelist_mask.txt \
    --node_map KG_node_map.txt \
    --saved_node_embeddings_path checkpoints/pretrain.ckpt \
    --best_ckpt checkpoints/patients_like_me.ckpt/patients_like_me.ckpt \
    --patient_aggr_nodes $patient_aggr_nodes
