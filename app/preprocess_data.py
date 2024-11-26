#%%
import utils
import json


def query_data(driver, limit = None):
    query = """
    MATCH (s:Biological_sample)
    OPTIONAL MATCH (s)-[:HAS_DAMAGE]->(g:Gene)
    where not g.synonyms[1]=""
    WITH s, collect(DISTINCT g.synonyms[1]) AS genes
    OPTIONAL MATCH (s)-[:HAS_PHENOTYPE]->(p:Phenotype)
    RETURN id(s) as id, genes as all_candidate_genes, collect(DISTINCT p.id) AS positive_phenotypes
    """ + (f"LIMIT {limit}" if limit else "")
    result = utils.request(driver, query)
    print(result)
    return result


def write_to_jsonline(data, file_name = "data.jsonl"):
    with open(file_name, "w") as f:
        for line in data:
            json_line = json.dumps(line)
            f.write(json_line + "\n")

def preprocess_data(driver,limit = None, file_name = None):
    data = query_data(driver, limit)
    driver.close()
    write_to_jsonline(data, file_name)




