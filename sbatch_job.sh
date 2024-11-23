#!/bin/bash

#SBATCH -J parprogprak1
#SBATCH -e /home/kurse/kurs00084/tb89zyce/ba/stderr/stderr.parprogprak1.%j.txt
#SBATCH -o /home/kurse/kurs00084/tb89zyce/ba/stdout/stdout.parprogprak1.%j.txt
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
# bash predict.sh
ls -a

echo "Job finished"
