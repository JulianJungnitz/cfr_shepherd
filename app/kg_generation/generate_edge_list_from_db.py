#%%
import os
import csv
import random
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import utils as utils



node_id_to_idx = {}
def load_node_map():
    node_map_file = "KG_node_map.txt"
    if not os.path.exists(node_map_file):
        print("Node map file not found. Please generate it first.")
        return

    with open(node_map_file, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            parts = line.strip().split("\t")
            if len(parts) < 2:
                continue
            idx, node_id_str = parts[0], parts[1]
            node_id_to_idx[int(node_id_str)] = int(idx)
    print(f"Loaded {len(node_id_to_idx)} nodes")
load_node_map()

#%%



def export_edge_list():
    driver = utils.connect_to_neo4j()
    node_ids = list(node_id_to_idx.keys())
    total_nodes = len(node_ids)
    print(f"Found {total_nodes} nodes in nodes map")

    file_name = "KG_edgelist_mask.txt"
    file_exists = os.path.exists(file_name)
    mode = "a" if file_exists else "w"

    start_chunk = 0
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            if len(lines) > 1:
                *_, last_line = lines
                last_idx_str = last_line.split("\t")[0]
                start_chunk = int(last_idx_str) + 1

    batch_size = 1000
    with open(file_name, mode, newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        if not file_exists:
            writer.writerow(["x_idx","y_idx","full_relation","mask"])

        chunk_count = (total_nodes // batch_size) + (1 if total_nodes % batch_size != 0 else 0)
        for chunk_idx, i in enumerate(range(0, total_nodes, batch_size)):
            if i < start_chunk:
                continue

            current_chunk = node_ids[i:i+batch_size]
            query = """
                MATCH (a)-[r]->(b)
                WHERE id(a) IN """ + str(current_chunk) + """
                RETURN
                    id(a) AS source_id,
                    Labels(a)[0] AS source_label,
                    type(r) AS rel_type,
                    id(b) AS target_id,
                    Labels(b)[0] AS target_label
                ORDER BY source_id, target_id
            """
            results = utils.execute_query(driver, query, debug=False)

            rows_to_write = []
            for row in results:
                s_id, t_id = row["source_id"], row["target_id"]
                if s_id not in node_id_to_idx or t_id not in node_id_to_idx:
                    continue
                x_idx = node_id_to_idx[s_id]
                y_idx = node_id_to_idx[t_id]
                rel_str = f"{row['source_label']};{row['rel_type']};{row['target_label']}"
                p = random.random()
                mask = "train" if p < 0.8 else "test" if p < 0.9 else "val"
                rows_to_write.append([x_idx, y_idx, rel_str, mask])

            writer.writerows(rows_to_write)
            print(f"Processed chunk {chunk_idx + 1} of {chunk_count}")

            f.flush()

if __name__ == "__main__":
    export_edge_list()