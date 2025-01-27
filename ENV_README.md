To run without the docker container use these steps:

conda env create -f ./app/SHEPHERD/original_environment.yml
bash ./app/SHEPHERD/install_pyg.sh       #or run the install_updated_pyg.sh to match pytorch>2.
pip install -U --no-deps -r cfr_requirements.txt 
pip install -U --no-deps -r ./app/additional_pip_requirements_shepherd.txt 

then run 
python ./app/test_shepherd.py


to have the app module available add the project_dir to the python path
local (linux):
export PYTHONPATH="/home/julian/Documents/cfr_shepherd:$PYTHONPATH"
local (mac):
export PYTHONPATH="/Users/julia/Library/Mobile Documents/com~apple~CloudDocs/Uni/Bachelorarbeit/code/cfr_shepherd:$PYTHONPATH"

on lichtenberg:
export PYTHONPATH="/home/jj56rivo/cfr_shepherd:$PYTHONPATH"
on CCRC
export PYTHONPATH="/dev/Julian/cfr_shepherd:$PYTHONPATH"

