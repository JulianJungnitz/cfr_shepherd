# %%
import yaml
import utils as utils
from preprocess_data import preprocess_data
import sys
from SHEPHERD.data_prep.shortest_paths import add_spl_to_patients
import subprocess
sys.path.insert(0, utils.SHEPHERD_DIR) 

def start_preprocessing_data(config):
    NUMBER_OF_SAMPLES_LIMIT = config["shepherd"]["NUMBER_OF_SAMPLES_LIMIT"]
    OVERWRITE_PREPROCESSED_DATA = config["shepherd"]["OVERWRITE_PREPROCESSED_DATA"]
    file_name = "./app/SHEPHERD/data/patients/hauner_data/data.jsonl"
    if(OVERWRITE_PREPROCESSED_DATA):
        print("Overwriting preprocessed data")
        LIMIT_SAMPLE_SIZE = config["shepherd"]["LIMIT_SAMPLE_SIZE"]
        NUMBER_OF_SAMPLES_LIMIT = NUMBER_OF_SAMPLES_LIMIT if LIMIT_SAMPLE_SIZE else None
        preprocess_data(driver, limit=NUMBER_OF_SAMPLES_LIMIT, file_name=file_name)
        print("Samples written to file: "+file_name)
    else:
        print("Not overwriting preprocessed data")

    generate_spl_matrix()


def generate_spl_matrix():
    path = utils.SHEPHERD_DIR + '/data_prep/shortest_paths'
    command = [
        'python',
        path + '/add_spl_to_patients.py',
        '--only_test_data',
    ]

    try:
        result = subprocess.run(
            command,
            text=True,
            check=True 
        )
        print('Command executed successfully.')
        print('Output:')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print('An error occurred while executing the command.')
        print('Return code:', e.returncode)
        print('Error output:')
        print(e.stderr)


    


def main():
    global driver

    print("Starting the program")
    driver = utils.connect_to_neo4j()

    config = utils.read_config()
    start_preprocessing_data(config)
    


if __name__ == "__main__":
    main()

# %%
