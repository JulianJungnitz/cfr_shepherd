#%%
import utils
import json
import os

from SHEPHERD.data_prep.shortest_paths import add_spl_to_patients
import subprocess

def query_data(driver, limit = None, ONLY_PATIENTS_WITH_DISEASE = False):
    query = """
    MATCH (s:Biological_sample) """ + ("" if ONLY_PATIENTS_WITH_DISEASE else """ OPTIONAL """) + """
    MATCH (s)-[:HAS_DISEASE]->(d:Disease)
    OPTIONAL MATCH (s)-[:HAS_DAMAGE]->(g:Gene)
    where not g.synonyms[1]=""
    WITH s, collect(DISTINCT g.synonyms[1]) AS genes
    OPTIONAL MATCH (s)-[:HAS_PHENOTYPE]->(p:Phenotype)
    RETURN id(s) as id, genes as all_candidate_genes, collect(DISTINCT p.id) AS positive_phenotypes
    """ + (f"LIMIT {limit}" if limit else "")
    result = utils.execute_query(driver, query)
    print(result)
    return result


def write_to_file(data, file_name = "data.txt"):
    if(os.path.exists(file_name)):
        os.remove(file_name)
    
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, "w") as f:
        for line in data:
            json_line = json.dumps(line)
            f.write(json_line + "\n")

def create_patients_data_file(driver,limit = None, file_name = None, ONLY_PATIENTS_WITH_DISEASE = False):
    data = query_data(driver, limit, ONLY_PATIENTS_WITH_DISEASE = ONLY_PATIENTS_WITH_DISEASE)
    driver.close()
    write_to_file(data, file_name)



def generate_spl_matrix():
    path = utils.SHEPHERD_DIR + '/data_prep/shortest_paths'
    command = [
        'python',
        path + '/add_spl_to_patients.py',
        '--only_test_data',
    ]
    utils.run_subprocess(command)



