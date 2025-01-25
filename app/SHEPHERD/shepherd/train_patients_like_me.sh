# Bash script to train SHEPHERD for patients-like-me
cd app/SHEPHERD/shepherd
patient_aggr_nodes=$1
patient_data=$2
checkpoint=$3
graph_shema=$4


# Command to run this bash script:
# bash run_patients_like_me.sh

# Command to run with the best hyperparameters from the paper
python train.py \
        --edgelist KG_edgelist_mask.txt \
        --node_map KG_node_map.txt \
        --patient_data $patient_data \
        --run_type patients_like_me \
        --saved_node_embeddings_path $checkpoint \
        --sparse_sample 300 \
        --lr 5e-05 \
        --upsample_cand 1 \
        --neighbor_sampler_size 15 \
        --lmbda 0.7 \
        --kappa 0.09000000000000001 \
        --patient_aggr_nodes $patient_aggr_nodes \
        --graph_shema $graph_shema 