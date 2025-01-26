# %%


import pandas as pd
import json
from tqdm import tqdm
from pronto import Ontology
from app.SHEPHERD import project_config
import pickle


def get_relations_of_node(file_path: str):
    node_id = 1
    print(f"Node ID: {node_id}")
    df = pd.read_csv(file_path, sep="\t", header=None)
    print("file read")

    # Get all relations of node_id
    relations_to = df[df[0] == node_id]
    relations_from = df[df[1] == node_id]

    node_id_str = str(node_id)
    relations_from_str = df[df[1] == node_id_str]
    relations_to_str = df[df[0] == node_id_str]

    # transform relations_from and relations_to to string
    relations_from = relations_from.astype(str)
    relations_to = relations_to.astype(str)

    relations_from = pd.concat([relations_from, relations_from_str])
    relations_to = pd.concat([relations_to, relations_to_str])

    # sort by node_id
    relations_to = relations_to.sort_values(by=0)
    relations_from = relations_from.sort_values(by=1)

    for i, row in relations_to.iterrows():
        print(f"{row[0]} - {row[1]} with relation {row[2]}")
    print("\n----------------------------------------------")
    for i, row in relations_from.iterrows():
        print(f"{row[1]} - {row[0]} with relation {row[2]}")

    print("Length of relations_to: ", len(relations_to))
    print("Length of relations_from: ", len(relations_from))


def add_reverse_edges(file_path: str):
    print("Adding reverse edges")
    df = pd.read_csv(file_path, sep="\t", header=0)
    df_reverse = df.copy()
    df_reverse[["x_idx", "y_idx"]] = df_reverse[["y_idx", "x_idx"]]
    # df_reverse["full_relation"] = df_reverse["full_relation"].apply(
    #     lambda r: ";".join([r.split(";")[2], r.split(";")[1], r.split(";")[0]]) if len(r.split(";")) == 3 else r
    # )
    df_combined = pd.concat([df, df_reverse], ignore_index=True)
    file_base = file_path.rsplit(".", 1)[0]
    df_combined.to_csv(file_base + "_with_rev.txt", sep="\t", header=True, index=False)


def convert_types(file_path: str):
    print("Converting types")
    df = pd.read_csv(file_path, sep="\t", header=0)
    print("length: ", len(df))
    df = df[df["x_idx"] != "y_idx"]
    print("length: ", len(df))
    print("file read")
    df["x_idx"] = pd.to_numeric(df["x_idx"], errors="raise")
    print("converted x_idx")
    df["y_idx"] = pd.to_numeric(df["y_idx"], errors="raise")
    print("converted y_idx")
    df.to_csv(file_path + "_conv.txt", sep="\t", header=True, index=False)


def add_headers(file_path: str):
    # x_idx	y_idx	full_relation	mask
    headers = ["x_idx", "y_idx", "full_relation", "mask"]
    df = pd.read_csv(file_path, sep="\t", header=None)
    df.columns = headers
    df.to_csv(file_path, sep="\t", header=True, index=False)


def list_all_relationship_types(file_path: str):
    df = pd.read_csv(file_path, sep="\t", header=None)
    print(df[2].unique())

    add_reverse_edges


import numpy as np


def read_spl_matrix(file_path: str):
    spl_matrix = np.load(file_path)
    print(spl_matrix.shape)
    print(spl_matrix[:100, :100])


def read_pkl_file(file_name: str):
    import pickle

    with open(file_name, "rb") as f:
        data = pickle.load(f)
        data_str = str(data)
        print(data_str[:1000])


def test_hpo_dict(file_name):
    import pickle
    from tqdm import tqdm

    with open(file_name, "rb") as f:
        data = pickle.load(f)

    hpo_term = "HP:0033373"
    print(data[hpo_term])
    # # print random HPO terms
    # for i in range(10):
    #     r  = np.random.randint(0, len(data))
    #     print(list(data.keys())[r])

    # hpo_numbers = sorted(int(k.split(":")[1]) for k in data.keys())
    # missing_sections = {}
    # print("HPO range:", hpo_numbers[0], hpo_numbers[-1])
    # print("Number of missing:", (hpo_numbers[-1] - hpo_numbers[0] + 1) - len(hpo_numbers))

    # prev = hpo_numbers[0]
    # for n in tqdm(hpo_numbers[1:], desc="Processing HPOs"):
    #     if n > prev + 1:
    #         missing_sections[prev + 1] = n - 1
    #     prev = n

    # print("Missing sections:", missing_sections)


def create_hpo_to_idx_dict():
    import numpy as np
    import pickle

    node_file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_node_map.txt"
    hpo_to_idx_dict = {}
    idx_to_hpo_dict = {}
    df = pd.read_csv(
        node_file,
        sep="\t",
    )
    print(df.head())
    phen_df = df[df["node_type"] == "Phenotype"]
    for i, row in phen_df.iterrows():
        hpo_to_idx_dict[row["node_name"]] = row["node_idx"]

    for k, v in hpo_to_idx_dict.items():
        idx_to_hpo_dict[v] = k

    save_file_hpo_to_idx_dict = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/hpo_to_idx_dict_hauner_graph_reduced_new.pkl"
    with open(save_file_hpo_to_idx_dict, "wb") as f:
        pickle.dump(hpo_to_idx_dict, f)

    save_file_idx_to_hpo_dict = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/idx_to_hpo_dict_hauner_graph_reduced_new.pkl"
    with open(save_file_idx_to_hpo_dict, "wb") as f:
        pickle.dump(idx_to_hpo_dict, f)


def create_ensembl_to_idx_dict():
    import numpy as np
    import pickle
    import pronto
    from tqdm import tqdm

    node_file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_node_map.txt"
    ensembl_to_idx_dict = {}
    df = pd.read_csv(
        node_file,
        sep="\t",
    )
    gene_df = df[df["node_type"] == "Gene"]
    print(gene_df.head())
    gen_id_to_ens = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/gene_id_to_ens.csv"
    gene_id_to_ens_df = pd.read_csv(gen_id_to_ens, sep=",")
    print(gene_id_to_ens_df.head())
    node_to_ensembl = {}
    for i, row in gene_id_to_ens_df.iterrows():
        node_to_ensembl[row["ens_id"]] = row["gene_id"]

        
    not_found = []

    for ens_id, gene_id in tqdm(node_to_ensembl.items()):
        matches = gene_df[gene_df["node_name"] == gene_id]["node_idx"]
        if len(matches) == 0:
            not_found.append(ens_id)
        else:
            ensembl_to_idx_dict[ens_id] = matches.values[0]

    print("Number of not found genes: ", len(not_found))
    print("Number of found genes: ", len(ensembl_to_idx_dict))

    
    save_file_ensembl_to_idx_dict = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/ensembl_to_idx_dict_hauner_graph_reduced_new.pkl"
    with open(save_file_ensembl_to_idx_dict, "wb") as f:
        pickle.dump(ensembl_to_idx_dict, f)


def transform_sim_patients(file):
    with open(file, 'r') as f:
        data = [json.loads(line) for line in f]
    diseases = set()
    for patient in tqdm(data, desc="transforming patients"):
        disease_id = patient.get('disease_id')
        patient['true_diseases'] = [disease_id] if disease_id else []
        diseases.add(disease_id)
    new_file = file.rsplit(".", 1)[0] + "_new.jsonl"
    disease_file = file.rsplit(".", 1)[0] + "_diseases.txt"
    # with open(  new_file, 'w') as f:
    #     for patient in data:
    #         json.dump(patient, f)
    #         f.write('\n')
    with open(disease_file, 'w') as f:
        for disease in diseases:
            f.write(disease + "\n")


def get_doid_to_mondo():
    mondo = Ontology(project_config.PROJECT_DIR / "mondo.obo")
    doid_to_mondo = {}
    for term in mondo.terms():
        for xref in term.xrefs:
            if xref.id.startswith("DOID:"):
                doid_to_mondo[xref.id] = term.id
    return doid_to_mondo

def get_mondo_to_doid():
    mondo = Ontology(project_config.PROJECT_DIR / "mondo.obo")
    mondo_to_doid = {}
    for term in mondo.terms():
        for xref in term.xrefs:
            if xref.id.startswith("DOID:"):
                mondo_id = term.id
                mondo_id = mondo_id.replace("MONDO:", "")
                mondo_id = str(int(mondo_id))
                mondo_to_doid[mondo_id] = xref.id
    return mondo_to_doid

def save_mondo_to_diod():
    mondo_to_doid = get_mondo_to_doid()
    with open(project_config.PROJECT_DIR / "mondo_to_doid.pkl", "wb") as f:
        pickle.dump(mondo_to_doid, f)

def load_mondo_to_doid():
    with open(project_config.PROJECT_DIR / "mondo_to_doid.pkl", "rb") as f:
        mondo_to_doid = pickle.load(f)
    return mondo_to_doid

def test_mapping():
    mondo_to_doid_dict = load_mondo_to_doid()
    diseases = []
    file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/patients/simulated_patients/simulated_patients_formatted_diseases.txt"
    with open(file, "r") as f:
        diseases = [line.strip() for line in f]
    found = 0
    not_found = []
    print_n = 5
    for disease in diseases:
        if(print_n > 0):
            print(disease)
            print_n -= 1
        if disease in mondo_to_doid_dict:
            found += 1
        else:
            not_found.append(disease)
    print("first 5 dict entries: ", list(mondo_to_doid_dict.items())[:5])
    print("Found: ", found)
    print("Not found: ", len(not_found))

if __name__ == "__main__":
    # save_mondo_to_diod()
    # test_mapping()
    # transform_sim_patients("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/patients/simulated_patients/simulated_patients_formatted.jsonl")
    # create_hpo_to_idx_dict()
    # create_ensembl_to_idx_dict()
    # test_hpo_dict(
    #     "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/hpo_to_idx_dict_hauner_graph_reduced_new.pkl"
    # )#

    new_file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/mondo_to_idx_dict_hauner_graph_reduced_new.pkl"
    
    read_pkl_file(
        new_file
    )
    # read_pkl_file(
    # "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/8.9.21_kg/mondo_to_idx_dict_8.9.21_kg.pkl"
    #     )
    # add_reverse_edges("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")
    # list_all_relationship_types("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")

    # add_headers("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")
    # convert_types("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask_rev.txt")
    # get_relations_of_node("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/8.9.21_kg/KG_edgelist_mask.txt")

    # file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/mondo_to_idx_dict_hauner_graph_reduced.pkl"
    # with open(file, "rb") as f:
    #     data = pickle.load(f)
        
    # # remove MONDO: prefix
    # new_data = {}
    # for k, v in data.items():
    #     new_data[k.replace("MONDO:", "")] = v
    
    
    # with open(new_file, "wb") as f:
    #     pickle.dump(new_data, f)
