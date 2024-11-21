#%%
import utils
import json


def query_data(driver):
    query = """
    MATCH (s:Biological_sample)
    OPTIONAL MATCH (s)-[:HAS_DAMAGE]->(g:Gene)
    where not g.synonyms[1]=""
    WITH s, collect(DISTINCT g.synonyms[1]) AS genes
    OPTIONAL MATCH (s)-[:HAS_PHENOTYPE]->(p:Phenotype)
    RETURN id(s) as id, genes as all_candidate_genes, collect(DISTINCT p.id) AS positive_phenotypes
    """
    result = utils.request(driver, query)
    print(result)
    return result


def write_to_jsonline(data):
    with open("data.jsonl", "w") as f:
        for line in data:
            json_line = json.dumps(line)
            f.write(json_line + "\n")

def main():
    driver = utils.get_driver()
    data = query_data(driver)
    driver.close()
    write_to_jsonline(data)




if __name__ == "__main__":
    main()