#%%
import sys
sys.path.append('../')
sys.path.append('../SHEPHERD/')
sys.path.append('app/SHEPHERD/')
import pandas as pd
from collections import defaultdict
import math
import utils
import project_config

NODE_FILE = project_config.PROJECT_DIR / "knowledge_graph/8.9.21_kg/KG_node_map.txt"
EDGE_FILE =  project_config.PROJECT_DIR / "knowledge_graph/8.9.21_kg/KG_edgelist_mask.txt"


def generate_shepherd_kg_in_neo4J():
    driver = utils.connect_to_neo4j(use_shepherd_db=True)
    
    data = utils.execute_query(driver, "MATCH (n) return n limit 1")
    print("Data: ", data)


    node_df = pd.read_csv(NODE_FILE, sep="\t")
    print(node_df.head())
#        node_idx node_id     node_type node_name node_source
# 0         0    9796  gene/protein    PHYHIP        NCBI
# 1         1    7918  gene/protein    GPANK1        NCBI
# 2 
    for i, row in node_df.iterrows():
        print(row)
        node_type = row['node_type']
        if("/" not in node_type):
            continue
        node_type = node_type.replace("/", "_")
        query = f"CREATE (n: {node_type}) SET n.node_idx = {row['node_idx']},n.node_id = {row['node_id']}, n.node_name = '{row['node_name']}', n.node_source = '{row['node_source']}'"
        utils.execute_query(driver, query, debug=False)

    edge_df = pd.read_csv(EDGE_FILE, sep="\t")
    print(edge_df.head())

# x_idx	y_idx	full_relation	mask
# 0	8889	gene/protein;protein_protein;gene/protein	train
# 1	2798	gene/protein;protein_protein;gene/protein	train
# 2	5646	gene/protein;protein_protein;gene/protein	train
# 3	11592	gene/protein;protein_protein;gene/protein	train
    skip_to_index = 445111
    BATCH_SIZE = 1000

    # Group the data by type1, relation, and type2
    data_groups = defaultdict(list)

    
    for row in edge_df.itertuples(index=True):
        i = row.Index
        if i < skip_to_index:
            continue

        full_relation = row.full_relation.split(";")
        type1 = full_relation[0].replace("/", "_")
        relation = full_relation[1]
        type2 = full_relation[2].replace("/", "_")

        key = (type1, relation, type2)
        data_groups[key].append({'x_idx': row.x_idx, 'y_idx': row.y_idx})

    print("Data groups: ", data_groups.keys())
    for (type1, relation, type2), data_list in data_groups.items():
        total_batches = math.ceil(len(data_list) / BATCH_SIZE)
        for batch_num in range(total_batches):
            print("Batch: ", batch_num)
            batch_data = data_list[batch_num * BATCH_SIZE:(batch_num + 1) * BATCH_SIZE]
            query = f"""
            UNWIND $data AS row
            MATCH (n1:{type1} {{node_idx: row.x_idx}}), (n2:{type2} {{node_idx: row.y_idx}})
            CREATE (n1)-[:{relation}]->(n2)
            """
            execute_batch_query(driver, query, parameters={'data': batch_data}, debug=False)


def execute_batch_query(driver, query, parameters=None, debug=False):
    if debug:
        print("Executing query:")
        print(query)
        if parameters:
            print("With parameters:")
            print(parameters)
    
    with driver.session() as session:
        result = session.run(query, parameters)
        return result.consume()



if __name__ == "__main__":
    generate_shepherd_kg_in_neo4J()