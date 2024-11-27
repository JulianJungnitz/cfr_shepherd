#!/bin/bash

source /opt/conda/etc/profile.d/conda.sh

conda activate shepherd

export PYTHONUNBUFFERED=1

exec python -u /app/main.py
