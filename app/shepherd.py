# %%
import yaml
import logging
import utils as utils
from preprocess_data import preprocess_data



def main():
    global logger
    global driver
    logger = utils.create_logger()

    logger.info("Starting the program")
    driver = utils.connect_to_neo4j()

    config = utils.read_config()
    NUMBER_OF_SAMPLES = config["NUMBER_OF_SAMPLES"]
    OVERWRITE_PREPROCESSED_DATA = config["OVERWRITE_PREPROCESSED_DATA"]
    
    if(OVERWRITE_PREPROCESSED_DATA):
        logger.info("Overwriting preprocessed data")
        LIMIT_SAMPLE_SIZE = config["LIMIT_SAMPLE_SIZE"]
        NUMBER_OF_SAMPLES = NUMBER_OF_SAMPLES if LIMIT_SAMPLE_SIZE else None
        preprocess_data(driver, limit=NUMBER_OF_SAMPLES, file_name="./SHEPHERD/data/patients/hauner_data/data.jsonl")



if __name__ == "__main__":
    main()

# %%
