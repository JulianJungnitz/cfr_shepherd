# %%
import utils
import json
import os
from pronto import Ontology

from SHEPHERD.data_prep.shortest_paths import add_spl_to_patients
import subprocess


def query_data(
    driver,
    limit=None,
    ONLY_PATIENTS_WITH_DISEASE=False,
    ONLY_PATIENTS_WITH_PHENOTYPES=False,
    ONLY_PATIENTS_WITH_GENES=False,
    USE_HAUNER_GRAPH=False
):
    if not USE_HAUNER_GRAPH:
        query = (
            """
        MATCH (s:Biological_sample) """
            + ("" if ONLY_PATIENTS_WITH_DISEASE else """ OPTIONAL """)
            + """
        MATCH (s)-[:HAS_DISEASE]->(d:Disease)
        """
            + ("" if ONLY_PATIENTS_WITH_GENES else """ OPTIONAL """)
            + """ MATCH (s)-[:HAS_DAMAGE]->(g:Gene)
        where not g.synonyms[1]=""
        WITH s, collect(DISTINCT g.synonyms[1]) AS genes, d
        """
            + ("" if ONLY_PATIENTS_WITH_PHENOTYPES else """ OPTIONAL """)
            + """ MATCH (s)-[:HAS_PHENOTYPE]->(p:Phenotype)
        RETURN id(s) as id, genes as all_candidate_genes, collect(DISTINCT p.id) AS positive_phenotypes, collect(DISTINCT d.id) AS true_diseases_doid_ids
        """
            + (f"LIMIT {limit}" if limit else "")
        )
        result = utils.execute_query(driver, query)
        doid_to_mondo = get_doid_to_mondo()
        return_result = []
        for record in result:
            mondo_ids = [
                doid_to_mondo.get(doid, None) for doid in record["true_diseases_doid_ids"]
            ]
            mondo_ids = [x.split(":")[1] for x in mondo_ids if x and ":" in x]
            mondo_ids = list(set(mondo_ids))
            if ONLY_PATIENTS_WITH_DISEASE and len(mondo_ids) == 0:
                continue
            record["true_diseases"] = mondo_ids
            del record["true_diseases_doid_ids"]
            return_result.append(record)
    else:
        query = (
            """
        MATCH (s:Biological_sample) """
            + ("" if ONLY_PATIENTS_WITH_DISEASE else """ OPTIONAL """)
            + """
        MATCH (s)-[:HAS_DISEASE]->(d:Disease)
        """
            + ("" if ONLY_PATIENTS_WITH_GENES else """ OPTIONAL """)
            + """ MATCH (s)-[:HAS_DAMAGE]->(g:Gene)
    
        WITH s, collect(DISTINCT g.id) AS genes, d
        """
            + ("" if ONLY_PATIENTS_WITH_PHENOTYPES else """ OPTIONAL """)
            + """ MATCH (s)-[:HAS_PHENOTYPE]->(p:Phenotype)
        RETURN id(s) as id, genes as all_candidate_genes, collect(DISTINCT p.id) AS positive_phenotypes, 
        collect(DISTINCT d.id) AS true_diseases
        """
            + (f"LIMIT {limit}" if limit else "")
        )
        result = utils.execute_query(driver, query)
        
        
    return result


def get_doid_to_mondo():
    mondo = Ontology("./app/SHEPHERD/data/mondo-rare.obo")
    doid_to_mondo = {}
    for term in mondo.terms():
        for xref in term.xrefs:
            if xref.id.startswith("DOID:"):
                doid_to_mondo[xref.id] = term.id
    return doid_to_mondo


def write_to_file(data, file_name="data.txt"):
    if os.path.exists(file_name):
        os.remove(file_name)

    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, "w") as f:
        for line in data:
            json_line = json.dumps(line)
            f.write(json_line + "\n")


def create_patients_data_file(
    driver,
    limit=None,
    file_name=None,
    ONLY_PATIENTS_WITH_DISEASE=False,
    ONLY_PATIENTS_WITH_PHENOTYPES=False,
    ONLY_PATIENTS_WITH_GENES=False,
    USE_HAUNER_GRAPH=False
):
    data = query_data(
        driver,
        limit,
        ONLY_PATIENTS_WITH_DISEASE=ONLY_PATIENTS_WITH_DISEASE,
        ONLY_PATIENTS_WITH_PHENOTYPES=ONLY_PATIENTS_WITH_PHENOTYPES,
        ONLY_PATIENTS_WITH_GENES=ONLY_PATIENTS_WITH_GENES,
        USE_HAUNER_GRAPH=USE_HAUNER_GRAPH
    )
    driver.close()
    write_to_file(data, file_name)


def generate_spl_matrix(graph_shema, use_sim_patients=False,):
    path = utils.SHEPHERD_DIR + "/data_prep/shortest_paths"
    command = [
        "python",
        path + "/add_spl_to_patients.py",
        "--graph_shema",
        graph_shema,
    ]
    if not use_sim_patients:
        command.append("--only_test_data",)
    
    utils.run_subprocess(command)


# %%
