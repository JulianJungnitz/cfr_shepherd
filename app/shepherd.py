# %%
import yaml
import sys
import subprocess

sys.path.insert(0, "./app")
import utils as utils

sys.path.insert(0, utils.SHEPHERD_DIR)
from preprocess_data import create_patients_data_file, generate_spl_matrix
from app.SHEPHERD.project_config import PROJECT_DIR


def start_preprocessing_data(config, USE_HAUNER_GRAPH):
    NUMBER_OF_SAMPLES_LIMIT = config["shepherd"]["NUMBER_OF_SAMPLES_LIMIT"]
    OVERWRITE_PREPROCESSED_DATA = config["shepherd"]["OVERWRITE_PREPROCESSED_DATA"]
    ONLY_PATIENTS_WITH_DISEASE = config["shepherd"]["ONLY_PATIENTS_WITH_DISEASE"]
    ONLY_PATIENTS_WITH_PHENOTYPES = config["shepherd"]["ONLY_PATIENTS_WITH_PHENOTYPES"]
    ONLY_PATIENTS_WITH_GENES = config["shepherd"]["ONLY_PATIENTS_WITH_GENES"]
    file_name = PROJECT_DIR / "patients/hauner_data/data.txt"
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
            USE_HAUNER_GRAPH=USE_HAUNER_GRAPH,
        )
        print("Samples written to file: " + file_name)
    else:
        print("Not overwriting preprocessed data")


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


def predict_disease_categorization(PATIENTS_AGGR_NODES=None, checkpoint_appendix="", graph_shema="primeKG"):
    dir = utils.SHEPHERD_DIR
    print("Predicting disease categorization. Dir: " + dir)
    command = ["bash", dir + "/predict_disease_categorization.sh", PATIENTS_AGGR_NODES, checkpoint_appendix, graph_shema]
    utils.run_subprocess(command)


def run_training_disease_characterization(config, PATIENTS_AGGR_NODES=None):
    print("Training disease characterization")
    data_type = "my_data"
    USE_SIMULATED_DATA = config["shepherd"]["USE_SIMULATED_PATIENTS"]
    if USE_SIMULATED_DATA:
        data_type = "disease_simulated"

    USE_HAUNER_GRAPH = config["shepherd"]["USE_HAUNER_GRAPH"]
    checkpoint = "checkpoints/pretrain.ckpt"
    if USE_HAUNER_GRAPH:
        checkpoint = "checkpoints/pretrain_hauner.ckpt"

    graph_shema = "hauner" if USE_HAUNER_GRAPH else "primeKG"
    command = [
        "bash",
        utils.SHEPHERD_DIR + "/shepherd/train_disease_characterization.sh",
        PATIENTS_AGGR_NODES,
        data_type,
        checkpoint,
        graph_shema,
    ]
    utils.run_subprocess(command)


def move_results_to_output_dir():
    print(
        "Moving results to output directory: res: "
        + utils.RESULTS_DIR
        + " out: "
        + utils.OUTPUT_DIR
    )
    resDir = utils.RESULTS_DIR
    outDir = utils.OUTPUT_DIR
    command = ["cp", "-r", resDir, outDir]
    utils.run_subprocess(command)


def run_shepherd_preprocessing(config,):
    print("Running shepherd preprocessing")
    dir = utils.SHEPHERD_DIR
    use_simulated_data = config["shepherd"]["USE_SIMULATED_PATIENTS"]

    command = [
        "python",
        dir + "/data_prep/preprocess_patients_and_kg.py",
        "-split_dataset",
    ]
    if not use_simulated_data:
        dataDir = PROJECT_DIR
        command.append(
            "-simulated_path",
        )
        command.append(
            dataDir + "/patients/hauner_data/data.txt",
        )
    utils.run_subprocess(command)


def run_pretraining(config):
    print("Running shepherd pretraining")
    dir = utils.SHEPHERD_DIR
    save_dir = utils.SCRATCH_DIR + "/pretrain"

    USE_HAUNER_GRAPH = config["shepherd"]["USE_HAUNER_GRAPH"]
    graph_shema = "hauner" if USE_HAUNER_GRAPH else "primeKG"
    command = [
        "python",
        dir + "/shepherd/pretrain.py",
        "--edgelist",
        "KG_edgelist_mask.txt",
        "--node_map",
        "KG_node_map.txt",
        "--save_dir",
        save_dir,
        "--graph_shema",
        graph_shema,
        # "--resume",
        # "resume_best_full_epoch_3",
        # "--best_ckpt",
        # "best_full_epoch_3.ckpt",
    ]
    utils.run_subprocess(command)

def run_training_patients_like_me(config, PATIENTS_AGGR_NODES=None):
    print("Training patients like me")
    data_type = "my_data"
    USE_SIMULATED_DATA = config["shepherd"]["USE_SIMULATED_PATIENTS"]
    if USE_SIMULATED_DATA:
        data_type = "disease_simulated"

    USE_HAUNER_GRAPH = config["shepherd"]["USE_HAUNER_GRAPH"]
    checkpoint = "checkpoints/pretrain.ckpt"
    if USE_HAUNER_GRAPH:
        checkpoint = "checkpoints/pretrain_hauner.ckpt"

    graph_shema = "hauner" if USE_HAUNER_GRAPH else "primeKG"
    command = [
        "bash",
        utils.SHEPHERD_DIR + "/shepherd/train_patients_like_me.sh",
        PATIENTS_AGGR_NODES,
        data_type,
        checkpoint,
        graph_shema,
    ]
    utils.run_subprocess(command)


def main():
    global driver

    print("Starting the program")
    driver = utils.connect_to_neo4j()

    config = utils.read_config()

    CREATE_SPL_MATRIX = config["shepherd"]["CREATE_SPL_MATRIX"]
    USE_SIMULATED_DATA = config["shepherd"]["USE_SIMULATED_PATIENTS"]
    USE_HAUNER_GRAPH = config["shepherd"]["USE_HAUNER_GRAPH"]
    checkpoint_appendix = "_hauner" if USE_HAUNER_GRAPH else ""
    graph_shema = "hauner" if USE_HAUNER_GRAPH else "primeKG"

    start_preprocessing_data(config,USE_HAUNER_GRAPH)

    
    if CREATE_SPL_MATRIX:
        generate_spl_matrix(
            "shepherd" if USE_HAUNER_GRAPH else "primeKG",
            use_sim_patients=USE_SIMULATED_DATA,
        )

    PATIENTS_AGGR_NODES = config["shepherd"]["PATIENTS_AGGR_NODES"]

    RUN_PRETRAINING = config["shepherd"]["RUN_PRETRAINING"]
    if RUN_PRETRAINING:
        run_pretraining(config)

    RUN_PREPROCESSING = config["shepherd"]["RUN_PREPROCESSING"]
    if RUN_PREPROCESSING:
        run_shepherd_preprocessing(config)

    RUN_TRAINING_DISEASE_CHARACTERIZATION = config["shepherd"][
        "RUN_TRAINING_DISEASE_CHARACTERIZATION"
    ]
    if RUN_TRAINING_DISEASE_CHARACTERIZATION:
        run_training_disease_characterization(config, PATIENTS_AGGR_NODES)

    RUN_TRAINING_PATIENTS_LIKE_ME = config["shepherd"]["RUN_TRAINING_PATIENTS_LIKE_ME"]
    if RUN_TRAINING_PATIENTS_LIKE_ME:
        run_training_patients_like_me(config, PATIENTS_AGGR_NODES)

    RUN_PATIENTS_LIKE_ME = config["shepherd"]["RUN_PATIENTS_LIKE_ME"]
    if RUN_PATIENTS_LIKE_ME:
        predict_patients_like_me(
            PATIENTS_AGGR_NODES,
        )

    RUN_CAUSAL_GENE_DISCOVERY = config["shepherd"]["RUN_CAUSAL_GENE_DISCOVERY"]
    if RUN_CAUSAL_GENE_DISCOVERY:
        predict_causal_gene_discovery()

    RUN_DISEASE_CATEGORIZATION = config["shepherd"]["RUN_DISEASE_CATEGORIZATION"]
    if RUN_DISEASE_CATEGORIZATION:
        predict_disease_categorization(
            PATIENTS_AGGR_NODES, checkpoint_appendix, graph_shema
        )

    MOVE_RESULTS_TO_OUTPUT_DIR = config["shepherd"]["MOVE_RESULTS_TO_OUTPUT_DIR"]
    if MOVE_RESULTS_TO_OUTPUT_DIR:
        move_results_to_output_dir()


# %%
