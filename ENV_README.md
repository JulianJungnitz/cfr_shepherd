To run without the docker container use these steps:

conda env create -f ./app/SHEPHERD/original_environment.yml
bash ./app/SHEPHERD/install_pyg.sh
pip install -U --no-deps -r cfr_requirements.txt 
pip install -U --no-deps -r ./app/additional_pip_requirements_shepherd.txt 

then run 
python ./app/test_shepherd.py


to have the app module available add the project_dir to the python path
local:
export PYTHONPATH="/home/julian/Documents/cfr_shepherd:$PYTHONPATH"
on lichtenberg:
export PYTHONPATH="/home/jj56rivo/cfr_shepherd:$PYTHONPATH"
