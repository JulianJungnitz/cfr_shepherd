
cd app/SHEPHERD/shepherd

patient_aggr_nodes=$1
checkpoint_appendix=$2

python predict.py \
    --run_type disease_characterization \
    --patient_data my_data \
    --edgelist KG_edgelist_mask.txt \
    --node_map KG_node_map.txt \
    --saved_node_embeddings_path checkpoints/pretrain${checkpoint_appendix}.ckpt \
    --best_ckpt checkpoints/disease_characterization${checkpoint_appendix}.ckpt \
    --patient_aggr_nodes $patient_aggr_nodes 
