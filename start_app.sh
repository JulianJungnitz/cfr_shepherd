#!/bin/bash

source /opt/conda/etc/profile.d/conda.sh

conda activate test_shepherd

python -u ./app/main.py
