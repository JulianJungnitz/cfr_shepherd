To run without the docker container use these steps:

conda env create -f ./app/SHEPHERD/original_env.yml
bash ./app/SHEPHERD/install_pyg.sh
pip install -U --no-deps -r cfr_requirements.txt 