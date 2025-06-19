#!/bin/bash

echo "Fixing PyTorch Geometric compatibility..."

# First, check current PyTorch version
python -c "import torch; print(f'Current PyTorch version: {torch.__version__}')"

# Uninstall incompatible PyTorch Geometric versions
pip uninstall torch-geometric torch-scatter torch-sparse torch-cluster torch-spline-conv -y

# Install compatible PyTorch Geometric for PyTorch 1.8.0
pip install torch-scatter==2.0.8 -f https://pytorch-geometric.com/whl/torch-1.8.0+cu102.html
pip install torch-sparse==0.6.11 -f https://pytorch-geometric.com/whl/torch-1.8.0+cu102.html
pip install torch-cluster==1.5.9 -f https://pytorch-geometric.com/whl/torch-1.8.0+cu102.html
pip install torch-spline-conv==1.2.1 -f https://pytorch-geometric.com/whl/torch-1.8.0+cu102.html
pip install torch-geometric==1.7.2

echo "PyTorch Geometric compatibility fixed!"
python -c "import torch; import torch_geometric; print(f'PyTorch: {torch.__version__}'); print(f'PyG: {torch_geometric.__version__}')" 