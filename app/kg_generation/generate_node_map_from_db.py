#%%
import os
import csv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import utils as utils


# To generate projection in neo4j:
# CALL gds.graph.project(
#   'hauner_projection_full_shepherd',
#   ['Biological_process', 'Tissue', 'Cellular_component', 
#    'Disease', 'Phenotype', 'Molecular_function', 'Modification', 
#    'Gene', 'Transcript', 'Chromosome', 'Protein', 'Peptide', 'Modified_protein',
#    'Complex', 'Known_variant', 'Clinically_relevant_variant',
#    'Functional_region', 'Metabolite', 'Pathway'],
   
#   '*'
# );

#These node types are removed: ["Clinical_variable", "Experimental_factor","Publication","GWAS_study","Project","Subject","Biological_sample"]
# Stil contains 12361023 nodes

# To write the component id: 
# CALL gds.wcc.write('hauner_projection_full_shepherd', {
#   writeProperty: 'wccComponentId'
# })
# YIELD nodePropertiesWritten, componentCount
# RETURN nodePropertiesWritten, componentCount;

# To clear the component id:
# CALL apoc.periodic.iterate(
#   "MATCH (n) WHERE n.wccComponentId is not null RETURN n",
#   "REMOVE n.wccComponentId",
#   { batchSize: 10000, parallel: false }
# )

# To check the components sizes:
# MATCH (n)
# WITH n.wccComponentId AS cId, count(*) AS size
# RETURN cId AS componentId, size
# ORDER BY size DESC limit 10

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------


def export_node_map():
    driver = utils.connect_to_neo4j()

    count_query = """
        MATCH (n)
        RETURN count(n) AS count
    """
    result_count = utils.execute_query(driver, count_query, debug=False)
    total_count = result_count[0]["count"]
    batch_size = 500000
    
    file_exists = os.path.exists("node_map.txt")
    
    last_idx = -1
    if file_exists:
        with open("node_map.txt", "r") as existing_file:
            lines = existing_file.readlines()
            if len(lines) > 1:
                *_, last_line = lines
                last_idx_str = last_line.split("\t")[0]
                last_idx = int(last_idx_str)


    mode = "a" if file_exists else "w"
    file_name = "KG_node_map.txt"

    with open(file_name, mode, newline="") as f:
        writer = csv.writer(f, delimiter="\t")

        if not file_exists:
            writer.writerow(["node_idx","node_id","node_type","node_name","node_source"])

        
        for skip in range(0, total_count, batch_size):
            query = f"""
                MATCH (n)
                    where n.wccComponentId = 0
                RETURN
                    id(n) AS node_id,
                    Labels(n)[0] AS node_type,
                    n.id AS node_name,
                    'neo4j_hauner' AS node_source
                ORDER BY id(n)
                SKIP {skip}
                LIMIT {batch_size}
            """
            results = utils.execute_query(driver, query, debug=False)
            for row in results:
                last_idx += 1
                writer.writerow([
                    last_idx,
                    row["node_id"],
                    row["node_type"],
                    row["node_name"],
                    row["node_source"]
                ])
                f.flush()
                if last_idx % 100 == 0:
                    print(f"Exported {last_idx} nodes")

if __name__ == "__main__":
    export_node_map()