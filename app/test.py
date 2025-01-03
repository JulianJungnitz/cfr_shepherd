#%%


import pandas as pd

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

    #transform relations_from and relations_to to string
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
    df["x_idx"] = pd.to_numeric(df["x_idx"], errors='raise')
    print("converted x_idx")
    df["y_idx"] = pd.to_numeric(df["y_idx"], errors='raise')
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
    print(spl_matrix[:10, :10])

if __name__ == "__main__":
    read_spl_matrix("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_shortest_path_matrix_onlyphenotypes.npy")
    # add_reverse_edges("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")
    # list_all_relationship_types("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")

    # add_headers("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")
    # convert_types("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask_rev.txt")
    # get_relations_of_node("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/8.9.21_kg/KG_edgelist_mask.txt")