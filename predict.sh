cd SHEPHERD

conda init
conda env create -f environment.yml
conda activate shepherd
bash install_pyg.sh


set -e

CURRENT_DIR=$(pwd)
ESCAPED_DIR=$(echo "$CURRENT_DIR" | sed 's/\//\\\//g')
CONFIG_FILE="project_config.py"
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: $CONFIG_FILE not found in the current directory."
    exit 1
fi

echo "Setting up project_config.py"
sed -i "s/^PROJECT_DIR *= *.*/PROJECT_DIR = Path(\"$ESCAPED_DIR\/data\")/" "$CONFIG_FILE"



cd shepherd

python predict.py \
    --run_type patients_like_me \
    --patient_data my_data          \
    --edgelist KG_edgelist_mask.txt     \
    --node_map KG_node_map.txt          \
    --saved_node_embeddings_path checkpoints/pretrain.ckpt    \
    --best_ckpt checkpoints/patients_like_me.ckpt/patients_like_me.ckpt