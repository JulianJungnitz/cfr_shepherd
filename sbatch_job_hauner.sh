#!/bin/bash
#SBATCH -A project02537
#SBATCH -J cfr_shepherd
#SBATCH --mail-user=julian.jungnitz@web.de
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH -e /work/home/jj56rivo/cfr_shepherd/out/e_%j.txt
#SBATCH -o /work/home/jj56rivo/cfr_shepherd/out/o_%j.txt

#SBATCH -n 1
#SBATCH --mem-per-cpu=50G
#SBATCH --time=2-00:00:00
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:h100



echo "Job started"

cd /home/vagrant/dev/Julian/cfr_shepherd

cd app/SHEPHERD

set -e

source /home/vagrant/miniconda3/etc/profile.d/conda.sh
# source ~/anaconda3/etc/profile.d/conda.sh

conda activate shepherd
# bash install_pyg.sh


export PYTHONPATH="/home/vagrant/dev/Julian/cfr_shepherd:$PYTHONPATH"
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"


conda activate v5_shepherd



echo "Memory usage before running predict.py:"
free -h

cd ../..
# bash app/SHEPHERD/predict_patients_like_me.sh phenotypes
# bash app/SHEPHERD/predict_causal_gene.sh
# bash app/SHEPHERD/predict_disease_categorization.sh phenotypes
python app/test_shepherd.py

echo "Memory usage after running predict.py:"
free -h


echo "Job finished"