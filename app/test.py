# %%


import pandas as pd
import json
from tqdm import tqdm
from pronto import Ontology
import sys
from app.SHEPHERD import project_config
from app import utils
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
        return data


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
    gen_id_to_ens = (
        "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/gene_id_to_ens.csv"
    )
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
    mondo_to_doid_dict = load_mondo_to_doid()
    ens_dict = load_ens_to_id_dict()
    orphanet_to_mondo = read_pkl_file(
        "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/preprocess/orphanet/orphanet_to_mondo_dict.pkl"
    )
    print(
        "First 5 dict entries O-mondo: ",
        {k: v for k, v in list(orphanet_to_mondo.items())[:5]},
    )
    print(
        "First 5 dict entries M-doid: ", {k: v for k, v in list(mondo_to_doid_dict.items())[:5]}
    )
    print("First 5 dict entries E-id: ", {k: v for k, v in list(ens_dict.items())[:5]})


    with open(file, "r") as f:
        data = [json.loads(line) for line in f]
    diseases = set()
    for patient in tqdm(data, desc="transforming patients"):
        disease_id = patient.get("disease_id")
        patient["positive_phenotypes"] = list(
            patient.get("positive_phenotypes", {}).keys()
        )
        diseases.add(disease_id)
    new_file = file.rsplit(".", 1)[0] + "_new.jsonl"
    disease_file = file.rsplit(".", 1)[0] + "_diseases.txt"

    new_data = []
    not_found = 0
    found_mondo = 0
    print_n = 5
    
    for patient in data:
        disease = int(patient.get("disease_id"))
        if disease in orphanet_to_mondo:
            found_mondo += 1
            mondo = orphanet_to_mondo[disease][0]
            # print("Mondo: ", mondo)
            if mondo in mondo_to_doid_dict:
                
                disease_id = mondo_to_doid_dict[mondo]
                patient["disease_id"] = disease_id
                patient["true_diseases"] = [disease_id] if disease_id else []
                new_data.append(patient)
            else:
                if print_n > 0:
                    print("Mondo not found: ", mondo)
                    print_n -= 1
                not_found += 1
        else:
            if print_n > 0:
                print("Disease not found: ", disease)
                print_n -= 1
            not_found += 1

    patients_withoute_true_genes = 0
    patients_without_candidate_genes = 0
    print_n = 5
    final_data = []
    kg_file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_node_map.txt"
    df = pd.read_csv(
        kg_file,
        sep="\t",
    )
    kg_genes = set(df[df["node_type"] == "Gene"]["node_name"])
    for patient in new_data:
        true_genes = patient.get("true_genes", [])
        candidate_genes = patient.get("all_candidate_genes", [])
        patient["true_genes"] = [ens_dict[g] for g in true_genes if g in ens_dict]
        patient["all_candidate_genes"] = [ens_dict[g] for g in candidate_genes if g in ens_dict]
        if len(patient["true_genes"]) == 0:
            patients_withoute_true_genes += 1
            if(print_n > 0):
                print("True genes not found: ", true_genes)
                print_n -= 1
        else:
            add_paitent = True
            for gene in patient["true_genes"]:
                if gene not in kg_genes:
                    add_paitent = False
                    print("Gene not in KG: ", gene)
            if add_paitent:
                final_data.append(patient)  
        if len(patient["all_candidate_genes"]) == 0:
            patients_without_candidate_genes += 1


    print("Patients without true genes: ", patients_withoute_true_genes)
    print("Patients without candidate genes: ", patients_without_candidate_genes)
    print("New data length: ", len(new_data))
    print("Not found: ", not_found)
    print("Found mondo: ", found_mondo)
    print("final data length: ", len(final_data))
    # with open(disease_file, 'w') as f:
    #     for disease in diseases:
    #         f.write(disease + "\n")

    with open(new_file, "w") as f:
        for patient in final_data:
            json.dump(patient, f)
            f.write("\n")


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

def get_ens_to_id_dict():
    driver = utils.connect_to_neo4j()
    query = 'Match (g:Gene) where not g.synonyms[1]="" return g.id as gene_id, g.synonyms[1] as ensembl_id'
    result = utils.execute_query(driver, query)
    ens_to_id_dict = {}
    print("Number of records: ", len(result))
    for record in result:
        ens_to_id_dict[record["ensembl_id"]] = record["gene_id"]
    return ens_to_id_dict

def save_ens_to_id_dict():
    ens_to_id_dict = get_ens_to_id_dict()
    with open(project_config.PROJECT_DIR / "ens_to_id_dict.pkl", "wb") as f:
        pickle.dump(ens_to_id_dict, f)

def load_ens_to_id_dict():
    with open(project_config.PROJECT_DIR / "ens_to_id_dict.pkl", "rb") as f:
        ens_to_id_dict = pickle.load(f)
    return ens_to_id_dict


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
    found_mondo = 0
    not_found = []
    print_n = 5
    for disease in diseases:
        if print_n > 0:
            print(disease)
            print_n -= 1
        if disease in orphanet_to_mondo:
            found_mondo += 1
            mondo = orphanet_to_mondo[disease]
            if mondo in mondo_to_doid_dict:
                found += 1

        else:
            not_found.append(disease)
    print("first 5 dict entries: ", list(mondo_to_doid_dict.items())[:5])
    print("Found: ", found)
    print("Found mondo: ", found_mondo)
    print("Not found: ", len(not_found))


def check_patients_data():
    file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/patients/simulated_patients/simulated_patients_formatted_new.jsonl"
    with open(file, "r") as f:
        data = [json.loads(line) for line in f]
        
    
    # check if all patients have true genes
    patients_withoute_true_genes = 0
    patients_without_candidate_genes = 0
    for patient in data:
        true_genes = patient.get("true_genes", [])
        candidate_genes = patient.get("all_candidate_genes", [])
        if len(true_genes) == 0:
            patients_withoute_true_genes += 1
        if len(candidate_genes) == 0:
            patients_without_candidate_genes += 1
    
    print("Patients without true genes: ", patients_withoute_true_genes)
    print("Patients without candidate genes: ", patients_without_candidate_genes)


def check_simulated_patients():
    path = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/patients/simulated_patients/simulated_patients_formatted_new.jsonl"
    with open(path, "r") as f:
        data = [json.loads(line) for line in f]
    print("Number of patients: ", len(data))
    # print("First patient: ", data[0])
    disease_counts = {}
    for patient in data:
        disease = patient.get("disease_id")
        if disease in disease_counts:
            disease_counts[disease] += 1
        else:
            disease_counts[disease] = 1
    
    # plot disease counts descending
    disease_counts = dict(sorted(disease_counts.items(), key=lambda item: item[1], reverse=True))
    # print("Disease counts: ", disease_counts)
    print("Number of diseases: ", len(disease_counts))

    diseases = set(disease_counts.keys())
    print("diseases len")

    out_file= "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/patients/simulated_patients/simulated_patients_diseases_doid.txt"

    with open(out_file, "w") as f:
        for disease in diseases:
            f.write(disease + "\n")
        

def compare_disease_sets():
    sim_pat_dis = project_config.PROJECT_DIR / "patients/simulated_patients_diseases_doid.txt"
    
    driver = utils.connect_to_neo4j()
    query = 'Match (d:Disease)<-[:HAS_DISEASE]-(b:Biological_sample) return d.id as disease_id'
    result = utils.execute_query(driver, query)
    db_diseases = set([record["disease_id"] for record in result])

    with open(sim_pat_dis, "r") as f:
        sim_pat_diseases = set([line.strip() for line in f])
    
    print("First 5 db diseases: ", list(db_diseases)[:5])
    print("First 5 sim_pat diseases: ", list(sim_pat_diseases)[:5])

    print("Number of diseases in db: ", len(db_diseases))
    print("Number of diseases in sim_pat: ", len(sim_pat_diseases))

    print("Diseases in db but not in sim_pat: ", len(db_diseases - sim_pat_diseases))
    print("Diseases in sim_pat but not in db: ", len(sim_pat_diseases - db_diseases))


if __name__ == "__main__":
    compare_disease_sets()
    # save_mondo_to_diod()
    # test_mapping()
    # save_ens_to_id_dict()
    # check_patients_data()
    # transform_sim_patients(
    #     "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/patients/simulated_patients/simulated_patients_formatted.jsonl"
    # )
    # create_hpo_to_idx_dict()
    # create_ensembl_to_idx_dict()
    # test_hpo_dict(
    #     "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/hpo_to_idx_dict_hauner_graph_reduced_new.pkl"
    # )#

    # file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/mondo_to_idx_dict_hauner_graph_reduced.pkl"
    # read_pkl_file(file)

    # new_file = "/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/mondo_to_idx_dict_hauner_graph_reduced_new.pkl"
    # pkl_file ="/home/julian/Downloads/hpo_to_idx_dict_hauner_graph_reduced.pkl"
    # hpo_dict = read_pkl_file(
    #     pkl_file
    # )
    # hpo_list= ['HP:0062653','HP:0002448', 'HP:0002497', 'HP:0001249', 'HP:0001263', 'HP:0001290', 'HP:0003698', 'HP:0009027', 'HP:0003202', 'HP:0000648', 'HP:0012747', 'HP:0000726', 'HP:0002376', 'HP:0020102', 'HP:0003298', 'HP:0008940', 'HP:0008843', 'HP:0001959']
    # print("HPO terms:", len(hpo_dict))
    # sorted_hpo_dict_keys = sorted(hpo_dict.keys())
    # print("First HPO term:", sorted_hpo_dict_keys[:1])
    # print("Last HPO term:", sorted_hpo_dict_keys[-1:])

    # # find a key that contains 2497
    # for k in sorted_hpo_dict_keys:
    #     if "2497" in k:
    #         print(k)
    #         break
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
    #     new_data[str(int(k.replace("MONDO:", "")))] = v

    # with open(new_file, "wb") as f:
    #     pickle.dump(new_data, f)

# %%
