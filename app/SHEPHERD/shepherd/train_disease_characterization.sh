cd app/SHEPHERD/shepherd
patient_aggr_nodes=$1
patient_data=$2
checkpoint=$3
graph_shema=$4
# Bash script to train SHEPHERD for novel disease characterization

# Command to run this bash script:
# bash run_disease_characterization.sh

# Command to run with the best hyperparameters from the paper
python train.py \
        --edgelist KG_edgelist_mask.txt \
        --node_map KG_node_map.txt \
        --patient_data $patient_data \
        --run_type disease_characterization \
        --saved_node_embeddings_path  $checkpoint \
        --sparse_sample 300 \
        --lr 1e-05 \
        --upsample_cand 3 \
        --neighbor_sampler_size 15 \
        --lmbda 0.9 \
        --kappa 0.029999999999999992 \
        --patient_aggr_nodes $patient_aggr_nodes \
        --graph_shema $graph_shema 
        # --do_inference \
        # --best_ckpt checkpoints/disease_characterization_hauner.ckpt
