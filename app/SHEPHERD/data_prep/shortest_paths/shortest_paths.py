import multiprocessing
import numpy as np
import sys
import time
import snap
from tqdm import tqdm
import pandas as pd
from functools import partial

# Extend sys.path for project imports
sys.path.insert(0, "../..")  
sys.path.insert(0, "../../..")
sys.path.insert(0, "../../../..")
from app.SHEPHERD import project_config

# Filenames
suffix = ""  # e.g., "_noGO"
edgelist_f = "KG_edgelist_mask%s.txt" % suffix
nodemap_f = "KG_node_map%s.txt" % suffix
spl_mat_all_f = "KG_shortest_path_matrix_chunked%s.npy" % suffix
spl_mat_onlyphenotypes_f = "KG_shortest_path_matrix_onlyphenotypes_chunked%s.npy" % suffix

print("Filenames:")
print(edgelist_f)
print(nodemap_f)
print(spl_mat_all_f)
print(spl_mat_onlyphenotypes_f)
print("Starting to calculate shortest paths...")

processes = multiprocessing.cpu_count()
print("Available processes:", processes)

# Load node map
node_map = pd.read_csv(project_config.KG_DIR / nodemap_f, sep="\t")
print("Node map loaded")

# Load the SNAP graph
snap_graph = snap.LoadEdgeList(
    snap.PUNGraph, str(project_config.KG_DIR / edgelist_f), 0, 1
)
print("Graph loaded")

t0 = time.time()

node_ids = np.sort([node.GetId() for node in snap_graph.Nodes()])
n_nodes = len(node_map)
print(n_nodes, len(list(snap_graph.Nodes())), len(node_ids))
print(f"There are {n_nodes} nodes in the graph")
assert max(node_ids) == n_nodes - 1
print("Node IDs are sorted and start from 0")
if "noGO" not in edgelist_f:
    assert len(node_map) == len(node_ids)
print("Node map has the same number of nodes as the graph")


def get_shortest_paths_for_chunk(node_chunk, snap_graph, n_nodes):
    """Compute shortest paths for all node_ids in node_chunk."""
    chunk_results = []
    for node_id in node_chunk:
        NIdToDistH = snap.TIntH()
        snap.GetShortPath(snap_graph, int(node_id), NIdToDistH)
        paths = np.zeros(n_nodes)
        for dest_node in NIdToDistH:
            paths[dest_node] = NIdToDistH[dest_node]
        chunk_results.append(paths)
    return chunk_results


def process_chunk(chunk,  n_nodes):
    """Wrapper to call get_shortest_paths_for_chunk."""
    return get_shortest_paths_for_chunk(chunk, snap_graph, n_nodes)


# Chunk the node IDs to reduce overhead
chunk_size = 100
node_chunks = [node_ids[i : i + chunk_size] for i in range(0, len(node_ids), chunk_size)]

all_results = []

# Create a partial function carrying snap_graph and n_nodes
func = partial(process_chunk,  n_nodes=n_nodes)

# Multiprocessing pool: each worker processes a chunk of node IDs
with multiprocessing.Pool(processes=processes) as pool:
    print("Starting multiprocessing")
    for chunk_output in tqdm(
        pool.imap_unordered(func, node_chunks),
        total=len(node_chunks),
        desc="Processing Chunks"
    ):
        all_results.extend(chunk_output)

all_shortest_paths = np.stack(all_results)
print(all_shortest_paths.shape)
t1 = time.time()
print(f"It took {t1 - t0:0.4f}s to calculate the shortest paths")

# Save all shortest paths (requires no missing nodes)
if "noGO" not in spl_mat_all_f:
    np.save(project_config.KG_DIR / spl_mat_all_f, all_shortest_paths)
    print("Saved all shortest paths")

# Subset to shortest paths from all nodes to phenotypes
print("Subsetting to only phenotypes")
desired_idx = node_map[node_map["node_type"] == "Phenotype"]["node_idx"].tolist()
print("Desired index found")
try:
    print("Len:", len(desired_idx))
except Exception as e:
    print(e)
    print("Failed to get length of desired_idx")

all_shortest_paths_to_phens = all_shortest_paths[:, desired_idx]
with open(project_config.KG_DIR / spl_mat_onlyphenotypes_f, "wb") as f:
    np.save(f, all_shortest_paths_to_phens)
print("Saved shortest paths to phenotypes")