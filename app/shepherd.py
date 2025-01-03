# %%
import yaml
import sys
import subprocess

sys.path.insert(0, "./app")
import utils as utils

sys.path.insert(0, utils.SHEPHERD_DIR)
from preprocess_data import create_patients_data_file, generate_spl_matrix


def start_preprocessing_data(config):
    NUMBER_OF_SAMPLES_LIMIT = config["shepherd"]["NUMBER_OF_SAMPLES_LIMIT"]
    OVERWRITE_PREPROCESSED_DATA = config["shepherd"]["OVERWRITE_PREPROCESSED_DATA"]
    ONLY_PATIENTS_WITH_DISEASE = config["shepherd"]["ONLY_PATIENTS_WITH_DISEASE"]
    ONLY_PATIENTS_WITH_PHENOTYPES = config["shepherd"]["ONLY_PATIENTS_WITH_PHENOTYPES"]
    ONLY_PATIENTS_WITH_GENES = config["shepherd"]["ONLY_PATIENTS_WITH_GENES"]
    file_name = utils.SHEPHERD_DIR + "/data/patients/hauner_data/data.txt"
    if OVERWRITE_PREPROCESSED_DATA:
        print("Overwriting preprocessed data")
        LIMIT_SAMPLE_SIZE = config["shepherd"]["LIMIT_SAMPLE_SIZE"]
        NUMBER_OF_SAMPLES_LIMIT = NUMBER_OF_SAMPLES_LIMIT if LIMIT_SAMPLE_SIZE else None
        create_patients_data_file(
            driver,
            limit=NUMBER_OF_SAMPLES_LIMIT,
            file_name=file_name,
            ONLY_PATIENTS_WITH_DISEASE=ONLY_PATIENTS_WITH_DISEASE,
            ONLY_PATIENTS_WITH_PHENOTYPES=ONLY_PATIENTS_WITH_PHENOTYPES,
            ONLY_PATIENTS_WITH_GENES=ONLY_PATIENTS_WITH_GENES,
        )
        print("Samples written to file: " + file_name)
    else:
        print("Not overwriting preprocessed data")
    CREATE_SPL_MATRIX = config["shepherd"]["CREATE_SPL_MATRIX"]
    if CREATE_SPL_MATRIX:
        generate_spl_matrix()


def predict_patients_like_me(
    PATIENTS_AGGR_NODES=None, 
):
    dir = utils.SHEPHERD_DIR
    print("Predicting patients like me. Dir: " + dir)
    command = ["bash", dir + "/predict_patients_like_me.sh", PATIENTS_AGGR_NODES]
    utils.run_subprocess(command)


def predict_causal_gene_discovery():
    dir = utils.SHEPHERD_DIR
    print("Predicting causal gene discovery. Dir: " + dir)
    command = [
        "bash",
        dir + "/predict_causal_gene.sh",
    ]
    utils.run_subprocess(command)


def predict_disease_categorization(
    PATIENTS_AGGR_NODES=None
):
    dir = utils.SHEPHERD_DIR
    print("Predicting disease categorization. Dir: " + dir)
    command = ["bash", dir + "/predict_disease_categorization.sh", PATIENTS_AGGR_NODES]
    utils.run_subprocess(command)


def run_training_disease_characterization(PATIENTS_AGGR_NODES=None):
    print("Training disease characterization")
    command = [
        "bash",
        utils.SHEPHERD_DIR + "/shepherd/train_disease_characterization.sh",
        PATIENTS_AGGR_NODES,
    ]
    utils.run_subprocess(command)


def move_results_to_output_dir():
    print("Moving results to output directory: res: " + utils.RESULTS_DIR + " out: " + utils.OUTPUT_DIR)
    resDir = utils.RESULTS_DIR
    outDir = utils.OUTPUT_DIR
    command = ["cp", "-r", resDir, outDir]
    utils.run_subprocess(command)


def run_shepherd_preprocessing(config):
    print("Running shepherd preprocessing")
    dir = utils.SHEPHERD_DIR
    command = [
        "python",
        dir + "/data_prep/preprocess_patients_and_kg.py",
        "-split_dataset",
        "-simulated_path",
        dir + "/data/patients/hauner_data/data.txt",
    ]
    utils.run_subprocess(command)


def main():
    global driver

    print("Starting the program")
    driver = utils.connect_to_neo4j()

    config = utils.read_config()
    start_preprocessing_data(config)
    PATIENTS_AGGR_NODES = config["shepherd"]["PATIENTS_AGGR_NODES"]

    RUN_PREPROCESSING = config["shepherd"]["RUN_PREPROCESSING"]
    if RUN_PREPROCESSING:
        run_shepherd_preprocessing(config)

    RUN_TRAINING_DISEASE_CHARACTERIZATION = config["shepherd"][
        "RUN_TRAINING_DISEASE_CHARACTERIZATION"
    ]
    if RUN_TRAINING_DISEASE_CHARACTERIZATION:
        run_training_disease_characterization(PATIENTS_AGGR_NODES)

    RUN_PATIENTS_LIKE_ME = config["shepherd"]["RUN_PATIENTS_LIKE_ME"]
    if RUN_PATIENTS_LIKE_ME:
        predict_patients_like_me(
            PATIENTS_AGGR_NODES,
        )

    RUN_CAUSAL_GENE_DISCOVERY = config["shepherd"]["RUN_CAUSAL_GENE_DISCOVERY"]
    if RUN_CAUSAL_GENE_DISCOVERY:
        predict_causal_gene_discovery(
        )

    RUN_DISEASE_CATEGORIZATION = config["shepherd"]["RUN_DISEASE_CATEGORIZATION"]
    if RUN_DISEASE_CATEGORIZATION:
        predict_disease_categorization(
            PATIENTS_AGGR_NODES,
        )

    MOVE_RESULTS_TO_OUTPUT_DIR = config["shepherd"]["MOVE_RESULTS_TO_OUTPUT_DIR"]
    if MOVE_RESULTS_TO_OUTPUT_DIR:
        move_results_to_output_dir()


# %%
