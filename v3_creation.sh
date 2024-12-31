#!/bin/bash
#SBATCH -A project02537
#SBATCH -J cfr_shepherd
#SBATCH --mail-user=julian.jungnitz@web.de
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH -e /work/home/jj56rivo/cfr_shepherd/out/e_%j.txt
#SBATCH -o /work/home/jj56rivo/cfr_shepherd/out/o_%j.txt

#SBATCH -n 1
#SBATCH --mem-per-cpu=100G
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=1

echo "Job started"

conda env create -f v3_shepherd.yml

conda env list

echo "Job finished"