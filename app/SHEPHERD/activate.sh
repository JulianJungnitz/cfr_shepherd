#!/bin/bash
echo "Activating Shepherd environment"

# Ensure Conda is initialized
source ~/anaconda3/etc/profile.d/conda.sh

conda activate shepherd
export PYTHONPATH=$PYTHONPATH:$(pwd)
