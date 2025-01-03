import multiprocessing
import numpy as np
import sys
import time
import snap
from tqdm import tqdm
import pandas as pd

# sys.path.insert(0, '..') # add config to path
sys.path.insert(0, "../..")  # add config to path
sys.path.insert(0, "../../..")  # add config to path
sys.path.insert(0, "../../../..")  # add config to path
from app.SHEPHERD import project_config

# Filenames
suffix = ""  # or "_noGO"
edgelist_f = "KG_edgelist_mask%s.txt" % suffix
nodemap_f = "KG_node_map%s.txt" % suffix
spl_mat_onlyphenotypes_f = "KG_shortest_path_matrix_onlyphenotypes%s.npy" % suffix

print("Filenames :")
print(" Edgelist  :", edgelist_f)
print(" Node map   :", nodemap_f)
print(" Pheno file :", spl_mat_onlyphenotypes_f)

print("Starting to calculate shortest paths (PHENOTYPE NODES ONLY)...")

processes = multiprocessing.cpu_count()
print("Available processes:", processes)

# INPUT KG FILE
node_map = pd.read_csv(project_config.KG_DIR / nodemap_f, sep="\t")
snap_graph = snap.LoadEdgeList(
    snap.PUNGraph, str(project_config.KG_DIR / edgelist_f), 0, 1
)

node_ids = np.sort([node.GetId() for node in snap_graph.Nodes()])
n_nodes = len(node_map)

print(f"Total nodes in graph: {n_nodes}")
assert max(node_ids) == n_nodes - 1
print("Node IDs are sorted and start from 0")

# Identify phenotype nodes
phenotype_ids = node_map[node_map["node_type"] == "Phenotype"]["node_idx"].tolist()
phenotype_ids = np.sort(phenotype_ids)
n_phenotypes = len(phenotype_ids)
print(f"Found {n_phenotypes} phenotype nodes")

def get_shortest_path(src_id):
    NIdToDistH = snap.TIntH()
    snap.GetShortPath(snap_graph, int(src_id), NIdToDistH)
    paths = np.full(n_nodes, fill_value=-1, dtype=np.int32)  # or 0 if you prefer
    for dest_node in NIdToDistH:
        paths[dest_node] = NIdToDistH[dest_node]
    return paths

t0 = time.time()

# Run BFS only for phenotype nodes
with multiprocessing.Pool(processes=processes) as pool:
    print(f"Using {pool._processes} processes.")
    print("Starting multiprocessing BFS from phenotype nodes only...")
    # This will yield M BFS results, each BFS result is length n_nodes
    shortest_paths_from_phens = []
    for dist_array in tqdm(pool.imap_unordered(get_shortest_path, phenotype_ids),
                           total=n_phenotypes,
                           desc="Processing Phenotype Nodes"):
        shortest_paths_from_phens.append(dist_array)

print("Finished multiprocessing")

# Convert list to an (M x N) array: BFS-from-phenotypes to all nodes
all_shortest_paths = np.stack(shortest_paths_from_phens)  # shape = (M, N)
print("Shape of BFS results (pheno->all):", all_shortest_paths.shape)

# Now subset the columns so we only keep distances to phenotype nodes
# This yields an M x M matrix (phenotype->phenotype)
all_shortest_paths_to_phens = all_shortest_paths[:, phenotype_ids]
print("Shape of BFS results (pheno->pheno):", all_shortest_paths_to_phens.shape)

t1 = time.time()
print(f"It took {t1 - t0:.4f}s to calculate the phenotype-only shortest paths")

# Save only the phenotype->phenotype matrix
with open(project_config.KG_DIR / spl_mat_onlyphenotypes_f, "wb") as f:
    np.save(f, all_shortest_paths_to_phens)

print("Saved shortest path matrix for phenotype->phenotype only!")



