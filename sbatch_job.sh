#!/bin/bash


# remove old output files


#SBATCH -J parprogprak1
#SBATCH -e /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd/e.txt
#SBATCH -o /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd/o.txt
#SBATCH -C avx512
#SBATCH -n 1
#SBATCH --mem-per-cpu=1024
#SBATCH --time=5
#SBATCH --cpus-per-task=1
#SBATCH -A kurs00084
#SBATCH -p kurs00084
#SBATCH --reservation=kurs00084

rm /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd/e.txt
rm /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd/o.txt

echo "Job started"

cd /work/scratch/kurse/kurs00084/tb89zyce/ba/cfr_shepherd
bash predict.sh

echo "Job finished"
