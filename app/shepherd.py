# %%
import yaml
import sys
import subprocess
sys.path.insert(0, './app')
import utils as utils
sys.path.insert(0, utils.SHEPHERD_DIR) 
from preprocess_data import create_patients_data_file, generate_spl_matrix


def start_preprocessing_data(config):
    NUMBER_OF_SAMPLES_LIMIT = config["shepherd"]["NUMBER_OF_SAMPLES_LIMIT"]
    OVERWRITE_PREPROCESSED_DATA = config["shepherd"]["OVERWRITE_PREPROCESSED_DATA"]
    file_name = "./SHEPHERD/data/patients/hauner_data/data.txt"
    if(OVERWRITE_PREPROCESSED_DATA):
        print("Overwriting preprocessed data")
        LIMIT_SAMPLE_SIZE = config["shepherd"]["LIMIT_SAMPLE_SIZE"]
        NUMBER_OF_SAMPLES_LIMIT = NUMBER_OF_SAMPLES_LIMIT if LIMIT_SAMPLE_SIZE else None
        create_patients_data_file(driver, limit=NUMBER_OF_SAMPLES_LIMIT, file_name=file_name)
        print("Samples written to file: "+file_name)
    else:
        print("Not overwriting preprocessed data")
    CREATE_SPL_MATRIX = config["shepherd"]["CREATE_SPL_MATRIX"]
    if(CREATE_SPL_MATRIX):
       generate_spl_matrix()

def predict_patients_like_me():
    dir = utils.SHEPHERD_DIR 
    print("Predicting patients like me. Dir: "+dir)
    command = [
        'bash',
        dir + '/predict_patients_like_me.sh',
        
    ]
    utils.run_subprocess(command)




    


def main():
    global driver

    print("Starting the program")
    driver = utils.connect_to_neo4j()

    config = utils.read_config()
    start_preprocessing_data(config)

    predict_patients_like_me()


    


if __name__ == "__main__":
    main()

# %%
