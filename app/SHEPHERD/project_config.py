from pathlib import Path
import os

from app.utils import read_config



def is_running_in_docker():
    if os.path.exists('/.dockerenv'):
        return True
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            for line in f:
                if 'docker' in line:
                    return True
    except Exception:
        pass
    return False

if is_running_in_docker():
    INPUT_DIR = '/mnt/input'
    OUTPUT_DIR = '/mnt/output'
    print("Running inside Docker container.")
else:
    INPUT_DIR = './..'
    OUTPUT_DIR = './..'
    print("Running on local machine.")
current_dir = os.path.dirname(os.path.realpath(__file__))


#PROJECT_DIR = Path("/home/ema30/zaklab/rare_disease_dx/test_camera_ready") # Path('PATH/TO/SHEPHERD')
if(is_running_in_docker()):
    PROJECT_DIR = Path("/app/SHEPHERD/data")
elif "jj56rivo" in current_dir:
    print("Running on cluster")
    PROJECT_DIR = Path("/work/scratch/jj56rivo/cfr_shepherd_data")
else:
    PROJECT_DIR = Path("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data")

config = read_config()
print("Config: ", config)

if(config["shepherd"]["USE_HAUNER_GRAPH"]):
    CURR_KG = 'hauner_graph_reduced'
else:
    CURR_KG = '8.9.21_kg' 
print("Using knowledge graph: ", CURR_KG)

KG_DIR = PROJECT_DIR / 'knowledge_graph' / CURR_KG
PREDICT_RESULTS_DIR = PROJECT_DIR / 'results'
SEED = 33

# Modify the following variables for your dataset
MY_DATA_DIR = Path("hauner_data")
MY_TRAIN_DATA = MY_DATA_DIR / f"disease_split_train_sim_patients_{CURR_KG}.txt"
MY_VAL_DATA = MY_DATA_DIR / f"disease_split_val_sim_patients_{CURR_KG}.txt"
CORRUPT_TRAIN_DATA = MY_DATA_DIR / f"disease_split_train_sim_patients_{CURR_KG}_phencorrupt.txt"
CORRUPT_VAL_DATA = MY_DATA_DIR / f"disease_split_val_sim_patients_{CURR_KG}_phencorrupt.txt"

#MY_TRAIN_DATA = MY_DATA_DIR / f"disease_split_all_sim_patients_{CURR_KG}.txt"
#MY_VAL_DATA = "/n/data1/hms/dbmi/zaklab/mli/rare_disease_diagnosis/test_camera_ready/data/patients/mygene2_patients/mygene2_5.7.22_max250candgenes.txt"

MY_TEST_DATA = MY_DATA_DIR / "data.txt"
MY_SPL_DATA = MY_DATA_DIR / "disease_split_all_sim_patients_kg_8.9.21_kg_agg=mean_spl_matrix.npy"
MY_SPL_INDEX_DATA = MY_DATA_DIR / "disease_split_all_sim_patients_kg_8.9.21_kg_spl_index_dict.pkl"

# Exomiser
# MY_TEST_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_exomiser_distractor_genes_5_candidates_mapped_only_genes.txt" # MY_DATA_DIR / "PATH/TO/YOUR/DATA"
# MY_SPL_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_exomiser_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_matrix.npy" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_matrix.npy)
# MY_SPL_INDEX_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_exomiser_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_index_dict.pkl" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_index_dict.pkl)

# Curated
#MY_TEST_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_manual_baylor_nobgm_distractor_genes_5_candidates_mapped_only_genes.txt" # MY_DATA_DIR / "PATH/TO/YOUR/DATA"
#MY_SPL_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_manual_baylor_nobgm_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_matrix.npy" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_matrix.npy)
#MY_SPL_INDEX_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_manual_baylor_nobgm_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_index_dict.pkl" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_index_dict.pkl)
