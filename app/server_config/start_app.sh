#!/bin/bash

source /opt/conda/etc/profile.d/conda.sh

conda activate test_shepherd

pip show numpy
pip show jsonnet
python --version
# export PYTHONUNBUFFERED=1

# exec python -u /app/main.py
