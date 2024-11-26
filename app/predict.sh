#!/bin/bash


# remove old output files


#SBATCH -J parprogprak1
#SBATCH -e /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd/e.txt
#SBATCH -o /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd/o.txt
#SBATCH -C avx512
#SBATCH -n 1
#SBATCH --mem-per-cpu=64G
#SBATCH --time=00:32:00
#SBATCH --cpus-per-task=4
#SBATCH -A kurs00084
#SBATCH -p kurs00084
#SBATCH --reservation=kurs00084



echo "Job started"

# cd /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd
cd /home/julian/Documents/cfr_shepherd/

cd app/SHEPHERD

set -e

# source /work/scratch/kurse/kurs00084/tb89zyce/ba/miniconda3/etc/profile.d/conda.sh
source ~/anaconda3/etc/profile.d/conda.sh

conda activate shepherd
bash install_pyg.sh



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

echo "Memory usage before running predict.py:"
free -h

# start docker and run run predict

echo "Memory usage after running predict.py:"
free -h


echo "Job finished"