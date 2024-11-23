#!/bin/bash

#SBATCH -J parprogprak1
#SBATCH -e /work/scratch/kurse/kurs00084/tb89zyce/ba/output/e_%j.txt
#SBATCH -o /work/scratch/kurse/kurs00084/tb89zyce/ba/output/o_%j.txt
#SBATCH -C avx512
#SBATCH -n 1
#SBATCH --mem-per-cpu=1024
#SBATCH --time=5
#SBATCH --cpus-per-task=1
#SBATCH -A kurs00084
#SBATCH -p kurs00084
#SBATCH --reservation=kurs00084



echo "Job started"

cd /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd
bash predict.sh

echo "Job finished"
