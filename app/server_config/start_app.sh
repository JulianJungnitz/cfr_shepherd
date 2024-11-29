#!/bin/bash

source /opt/conda/etc/profile.d/conda.sh

conda activate test_shepherd

pip show numpy
pip show jsonnet
python --version
pip check  

python -u /app/main.py
