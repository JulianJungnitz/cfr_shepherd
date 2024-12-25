#%%


import pandas as pd

def read_unique_full_relation(file_path: str):
    print("read file")
    df = pd.read_csv(file_path, sep="\t")
    print("file read")
    unique_relations = df["full_relation"].unique()
    print("Unique full_relation values:")
    for relation in unique_relations:
        print(relation)

if __name__ == "__main__":
    read_unique_full_relation("/home/julian/Documents/cfr_shepherd/app/SHEPHERD/data/knowledge_graph/hauner_graph_reduced/KG_edgelist_mask.txt")