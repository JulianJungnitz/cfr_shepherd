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
    df = pd.read_csv(file_path, sep="\t", header=None)
    df = df.rename(columns={0: "source_node", 1: "target_node", 2: "relation"})
    print(df.head())
    print(df.shape)
    
    df_reverse = df.copy()
    df_reverse = df_reverse.rename(columns={"source_node": "target_node", "target_node": "source_node"})
    print(df_reverse.head())
    print(df_reverse.shape)
    df = pd.concat([df, df_reverse])
    print(df.shape)
    df.to_csv(file_path + "_with_rev.txt", sep="\t", header=False, index=False)

def convert_types(file_path: str):
    print("Converting types")
    df = pd.read_csv(file_path, sep="\t", header=None)
    print("file read")
    pd.to_numeric(df[0], errors='raise')
    print("converted 0")
    pd.to_numeric(df[1], errors='raise')
    print("converted 1")
    df.to_csv(file_path + "_conv.txt", sep="\t", header=False, index=False)

if __name__ == "__main__":
    convert_types("/work/scratch/jj56rivo/cfr_shepherd_data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask_rev.txt")
    # get_relations_of_node("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/8.9.21_kg/KG_edgelist_mask.txt")