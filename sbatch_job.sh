#!/bin/bash
#SBATCH -A project02537
#SBATCH -J cfr_shepherd
#SBATCH -e /work/home/jj56rivo/cfr_shepherd/out/e_%j.txt
#SBATCH -o /work/home/jj56rivo/cfr_shepherd/out/o_%j.txt

#SBATCH -n 1
#SBATCH --mem-per-cpu=200G
#SBATCH --time=12:00:00
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:v100



echo "Job started"

cd /work/home/jj56rivo/cfr_shepherd

cd app/SHEPHERD

set -e

source /work/home/jj56rivo/miniconda3/etc/profile.d/conda.sh
# source ~/anaconda3/etc/profile.d/conda.sh

conda activate shepherd
# bash install_pyg.sh


export PYTHONPATH="/home/jj56rivo/cfr_shepherd:$PYTHONPATH"


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