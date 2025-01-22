import json
import jsonlines
            
import sys
import pickle
from app.SHEPHERD import project_config
from app import utils
from pronto import Ontology
import pandas as pd


##############################################
# Read in/write patients

def read_patients(filename):
    patients = []
    with jsonlines.open(filename) as reader:
        for patient in reader:
            patients.append(patient)
    return patients


def write_patients(patients, filename):
    with open(filename, "w") as output_file:
        for patient_dict in patients:
            json.dump(patient_dict, output_file)
            output_file.write('\n')
            

def read_dicts():
    with open(project_config.KG_DIR / f'hpo_to_idx_dict_{project_config.CURR_KG}.pkl', 'rb') as handle:
        hpo_to_idx_dict = pickle.load(handle)

    with open(str(project_config.KG_DIR / f'ensembl_to_idx_dict_{project_config.CURR_KG}.pkl'), 'rb') as handle:
        ensembl_to_idx_dict = pickle.load(handle)

    with open(project_config.KG_DIR /  f'mondo_to_idx_dict_{project_config.CURR_KG}.pkl', 'rb') as handle:
        disease_to_idx_dict = pickle.load(handle)

    with open(str(project_config.PROJECT_DIR / 'preprocess' / 'orphanet' / 'orphanet_to_mondo_dict.pkl'), 'rb') as handle:
        orpha_mondo_map = pickle.load(handle)

    return hpo_to_idx_dict, ensembl_to_idx_dict, disease_to_idx_dict, orpha_mondo_map


def get_mondo_to_doid_dict():
    mondo_ontology = Ontology(project_config.PROJECT_DIR / 'mondo.obo')
    mondo_rare_ontology = Ontology(project_config.PROJECT_DIR / 'mondo-rare.obo')
    mondo_to_doid_dict = {}
    print('Creating mondo to DOID dict')
    for term in mondo_ontology.terms():
        if term.id.startswith("MONDO:"):
            for xref in term.xrefs:
                if xref.id.startswith("DOID:"):
                    mondo_to_doid_dict[term.name] = xref.id
                    break

    print("len mondo_to_doid_dict: ", len(mondo_to_doid_dict))

    for term in mondo_rare_ontology.terms():
        if term.id.startswith("MONDO:"):
            for xref in term.xrefs:
                if xref.id.startswith("DOID:"):
                    mondo_to_doid_dict[term.name] = xref.id
                    break

    print("len after rare dis: ", len(mondo_to_doid_dict))



    return mondo_to_doid_dict


def get_orphannet_to_mondo():
    file = utils.SHEPHERD_DIR + '/data_prep/orphanet_to_mondo_dict.pkl'
    orpha_mondo_map = pickle.load(open(file, 'rb'))
    
    return orpha_mondo_map

def get_orphannet_names_to_Id():
    file = utils.SHEPHERD_DIR + '/data_prep/orphanet_to_omim_mapping_df.csv'
    orpha_data = pd.read_csv(file, header=0)
    key_id = "Disorder_Name"
    val_id = "OrphaNumber"

    orpha_names_id_map  = dict(zip(orpha_data[key_id], orpha_data[val_id]))
    return orpha_names_id_map
