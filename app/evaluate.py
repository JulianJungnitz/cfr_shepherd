# %%
import pandas as pd
import utils as utils
import matplotlib.pyplot as plt
from app.SHEPHERD import project_config
import random
import pickle
import sys

from app.SHEPHERD import project_utils
from tqdm import tqdm
from pronto import Ontology


def evaluate_patients_like_me(score_file_path, min_dis_count=3):
    print(f"Evalute Patients Like me: {file}")
    df = pd.read_csv(score_file_path)

    df = filter_df_for_min_disease_count(df, min_disease_count=min_dis_count)

    patients_disease_map = get_all_patients_diseases(df)

    # print(f"Patients with diseases: {len(patients_with_disease)}")

    # filtered_df = df.filter(lambda x: x["patient_id"] in patients_with_disease)

    df = df.groupby("patient_id")
    print(df.head())

    patient_sim_map = {}
    max_k = 10
    for patient_id, group in df:
        for k in range(1, max_k + 1):
            (
                id_similar,
                icd10_similar,
                id_similar_random,
                icd10_similar_random,
                icd10_first_4_similarity_set,
                icd10_first_4_similarity_set_random,
            ) = get_patient_similarity_scores(
                patient_id, group, patients_disease_map, k=k
            )
            if patient_id not in patient_sim_map:
                patient_sim_map[patient_id] = {}
            patient_sim_map[patient_id][k] = {
                "id_similar": id_similar,
                "icd10_similar": icd10_similar,
                "id_similar_random": id_similar_random,
                "icd10_similar_random": icd10_similar_random,
                "icd10_first_4_similarity_set": icd10_first_4_similarity_set,
                "icd10_first_4_similarity_set_random": icd10_first_4_similarity_set_random,
            }

    number_of_patients = len(patient_sim_map)
    plot_patient_similarity_avg(
        patient_sim_map,
        max_k,
        score_file_path,
        number_of_patients=number_of_patients,
        min_dis_count=min_dis_count,
    )


def filter_df_for_min_disease_count(df, min_disease_count=3):
    query = f"""
    MATCH (n:Biological_sample)-[:HAS_DISEASE]->(d:Disease)
        WITH d, collect(n) AS samples
        WHERE size(samples) >= {min_disease_count}
        UNWIND samples AS sample
        RETURN id(sample) as sample_id"""

    driver = utils.connect_to_neo4j()
    res = utils.execute_query(driver, query, debug=False)
    patient_ids = [record["sample_id"] for record in res]
    print(
        f"Number of patients with at least {min_disease_count} diseases: ",
        len(patient_ids),
    )

    print("Original DF: ", len(df))
    df = df[df["patient_id"].isin(patient_ids)]
    print("Filtered DF: ", len(df))
    df = df[df["candidate_patients"].isin(patient_ids)]
    print("Filtered DF: ", len(df))

    return df


# def plot_patient_similarity(patient_sim_map,k_max):
#     patient_ids = list(patient_sim_map.keys())
#     k_values = range(1,  k_max+1)

#     for patient_id in patient_ids:
#         id_similarities = [patient_sim_map[patient_id][k]["id_similar"] for k in k_values]
#         icd10_similarities = [patient_sim_map[patient_id][k]["icd10_similar"] for k in k_values]

#         plt.figure(figsize=(10, 6))
#         plt.plot(k_values, id_similarities, label="ID Similarity")
#         plt.plot(k_values, icd10_similarities, label="ICD10 Similarity")

#         plt.title(f"Patient Similarity Scores for Patient ID: {patient_id}")
#         plt.xlabel("Top-K Similar Patients")
#         plt.ylabel("Similarity Count")
#         plt.xticks(k_values)
#         plt.yticks(range(0, 1))

#         plt.legend()
#         plt.grid(axis="y", linestyle="--", alpha=0.7)

#         # save to file
#         file = project_config.PROJECT_DIR / "plots" / f"patient_{patient_id}_similarity_scores.png"
#         print(f"Saving plot to {file}")
#         plt.savefig(file)


def plot_patient_similarity_avg(
    patient_sim_map, k_max, score_file_path, number_of_patients, min_dis_count
):
    patient_ids = list(patient_sim_map.keys())
    k_values = range(1, k_max + 1)

    len_patient_ids = len(patient_ids)
    k_icd10_similar_total = {k: 0 for k in k_values}
    k_id_similar_total = {k: 0 for k in k_values}
    k_icd10_similar_random_total = {k: 0 for k in k_values}
    k_id_similar_random_total = {k: 0 for k in k_values}
    k_icd10_first_4_similar_total = {k: 0 for k in k_values}
    k_icd10_first_4_similar_random_total = {k: 0 for k in k_values}

    for patient_id in patient_ids:
        for k in k_values:
            k_id_similar_total[k] += patient_sim_map[patient_id][k]["id_similar"]
            k_icd10_similar_total[k] += patient_sim_map[patient_id][k]["icd10_similar"]
            k_id_similar_random_total[k] += patient_sim_map[patient_id][k][
                "id_similar_random"
            ]
            k_icd10_similar_random_total[k] += patient_sim_map[patient_id][k][
                "icd10_similar_random"
            ]
            k_icd10_first_4_similar_total[k] += patient_sim_map[patient_id][k][
                "icd10_first_4_similarity_set"
            ]
            k_icd10_first_4_similar_random_total[k] += patient_sim_map[patient_id][k][
                "icd10_first_4_similarity_set_random"
            ]

    k_id_similar_avg = {k: k_id_similar_total[k] / number_of_patients for k in k_values}
    k_icd10_similar_avg = {
        k: k_icd10_similar_total[k] / number_of_patients for k in k_values
    }
    k_id_similar_random_avg = {
        k: k_id_similar_random_total[k] / number_of_patients for k in k_values
    }
    k_icd10_similar_random_avg = {
        k: k_icd10_similar_random_total[k] / number_of_patients for k in k_values
    }
    k_icd10_first_4_similar_avg = {
        k: k_icd10_first_4_similar_total[k] / number_of_patients for k in k_values
    }
    k_icd10_first_4_similar_random_avg = {
        k: k_icd10_first_4_similar_random_total[k] / number_of_patients
        for k in k_values
    }

    fig, ax = plt.subplots(
        figsize=(10, 6),
    )
    ax.plot(k_values, list(k_id_similar_avg.values()), label="ID Similar", color="blue")
    ax.plot(
        k_values,
        list(k_id_similar_random_avg.values()),
        label="ID Similar Random",
        color="blue",
        linestyle="--",
    )
    ax.plot(
        k_values,
        list(k_icd10_similar_avg.values()),
        label="ICD10 Similar",
        color="green",
    )
    ax.plot(
        k_values,
        list(k_icd10_similar_random_avg.values()),
        label="ICD10 Similar Random",
        color="green",
        linestyle="--",
    )
    ax.plot(
        k_values,
        list(k_icd10_first_4_similar_avg.values()),
        label="ICD10 First 5 Similar",
        color="red",
    )
    ax.plot(
        k_values,
        list(k_icd10_first_4_similar_random_avg.values()),
        label="ICD10 First 5 Similar Random",
        color="red",
        linestyle="--",
    )
    ax.set_xlabel("K")
    ax.set_ylabel("Similarity")
    ax.set_title(
        f"Patient Similarity Average of patient at rank k.\n At least one similar disease or icd10 code (min_dis_count: {min_dis_count})"
    )
    handles, labels = ax.get_legend_handles_labels()
    sorted_handles_labels = sorted(zip(handles, labels), key=lambda x: "Random" in x[1])
    sorted_handles, sorted_labels = zip(*sorted_handles_labels)
    ax.legend(sorted_handles, sorted_labels)
    file = (
        project_config.PROJECT_DIR
        / "plots"
        / f"patient_similarity_scores_min_d_{min_dis_count}_patients_len_{len_patient_ids}.png"
    )
    print(f"Saving plot to {file}")
    plt.savefig(file, format="png")


def get_patient_similarity_scores(patient_id, group, patients_disease_map, k=5):
    if patient_id not in patients_disease_map:
        print(f"Patient {patient_id} has no diseases")
        return 0, 0
    patient_disease = patients_disease_map[patient_id]
    id_similar = 0
    icd10_similar = 0
    index = k - 1
    # sort group by score
    group = group.sort_values(by="similarities", ascending=False)

    candidate_patient_id = int(group.iloc[index]["candidate_patients"])
    if candidate_patient_id not in patients_disease_map:
        return 0, 0
    candidate_patient_disease = patients_disease_map[candidate_patient_id]
    id_similarity_set = set(patient_disease["diseases"]).intersection(
        set(candidate_patient_disease["diseases"])
    )
    icd10_similarity_set = set(patient_disease["icd10_codes"]).intersection(
        set(candidate_patient_disease["icd10_codes"])
    )
    icd10_first_4_similarity_set = set(
        code[:10] for code in patient_disease["icd10_codes"]
    ).intersection(set(code[:10] for code in candidate_patient_disease["icd10_codes"]))

    random_patient_disease = patients_disease_map[
        random.choice(list(patients_disease_map.keys()))
    ]
    id_similarity_set_random = set(patient_disease["diseases"]).intersection(
        set(random_patient_disease["diseases"])
    )
    icd10_similarity_set_random = set(patient_disease["icd10_codes"]).intersection(
        set(random_patient_disease["icd10_codes"])
    )
    icd10_first_4_similarity_set_random = set(
        code[:10] for code in patient_disease["icd10_codes"]
    ).intersection(set(code[:10] for code in random_patient_disease["icd10_codes"]))

    # if len(id_similarity_set) > 0:
    #     print(f"Patient {patient_id} and Patient {candidate_patient_id} have similar diseases: {id_similarity_set}")
    # if len(icd10_similarity_set) > 0:
    #     print(f"Patient {patient_id} and Patient {candidate_patient_id} have similar icd10 codes: {icd10_similarity_set}")

    id_similar += len(id_similarity_set) > 0
    icd10_similar += len(icd10_similarity_set) > 0
    id_similar_random = len(id_similarity_set_random) > 0
    icd10_similar_random = len(icd10_similarity_set_random) > 0
    icd10_first_4_similarity = len(icd10_first_4_similarity_set) > 0
    icd10_first_4_similarity_random = len(icd10_first_4_similarity_set_random) > 0

    return (
        id_similar,
        icd10_similar,
        id_similar_random,
        icd10_similar_random,
        icd10_first_4_similarity,
        icd10_first_4_similarity_random,
    )


def get_all_patients_diseases(df):
    driver = utils.connect_to_neo4j()
    patient_ids = df["patient_id"].unique()
    candidate_patients = df["candidate_patients"].unique()
    all_patient_ids = list(patient_ids) + list(candidate_patients)
    print("Head: ", all_patient_ids[:5])
    # all_patient_ids = [x[0] for x in all_patient_ids]
    unique_patient_ids = list(set(all_patient_ids))

    query = f"""
    MATCH (p:Biological_sample)-[:HAS_DISEASE]->(d:Disease)
    WHERE id(p) in {unique_patient_ids}
    RETURN  id(p) as patient_id, 
    collect(id(d)) as diseases, 
    collect([syn IN d.synonyms WHERE syn STARTS WITH "ICD10"] )AS icd10_codes

    """
    res = utils.execute_query(driver, query, debug=False)

    for record in res:
        icd10_codes = record["icd10_codes"]
        icd10_codes = [item for sublist in icd10_codes for item in sublist]
        record["icd10_codes"] = icd10_codes

    patient_disease_map = {}
    for record in res:
        patient_id = record["patient_id"]
        diseases = record["diseases"]
        icd10_codes = record["icd10_codes"]
        patient_disease_map[patient_id] = {
            "diseases": diseases,
            "icd10_codes": icd10_codes,
        }

    return patient_disease_map


## DISEASE CHARACTERIZATION --------------------------------------------


def map_disease_to_doid(df):

    mondo_name_to_doid_dict = get_mondo_name_to_doid_dict()
    print("First mondo_name_to_doid_dict: ", {k: v for k, v in list(mondo_name_to_doid_dict.items())[:5]})
    print("Len: ", len(mondo_name_to_doid_dict))
    df["doid"] = df["diseases"].map(mondo_name_to_doid_dict)
    df = df[df["doid"].notnull()]
    df["doid_full"] = df["doid"]
    
    df["doid"] = df["doid"].apply(lambda x: str(int(x.split(":")[-1])))

    return df


def get_disease_patient_map(df):
    driver = utils.connect_to_neo4j()
    patient_ids = df["patient_id"].unique()

    diseases = df["doid_full"].unique()


    query = f"""
    MATCH (p:Biological_sample)-[:HAS_DISEASE]->(d:Disease)
    WHERE id(p) in {list(patient_ids)} AND d.id in {list(diseases)}
    RETURN id(p) as patient_id, d.id as disease_id
"""

    res = utils.execute_query(driver, query, debug=False)

    disease_patient_map = {}
    for record in res:
        patient_id = record["patient_id"]
        disease_id = record["disease_id"]
        stripped_disease= disease_id.split(":")[-1]
        disease_id = str(int(stripped_disease))
        if disease_id not in disease_patient_map:
            disease_patient_map[disease_id] = set()
        disease_patient_map[disease_id].add(patient_id)
    return disease_patient_map


def evaluate_disease_characterization(
    file_name,
):
    df = pd.read_csv(file_name)

    # return

    # df = map_disease_to_doid(df)
    df["doid_full"] = df["diseases"]
    df["doid"] = df["diseases"].apply(lambda x: str(int(x.split(":")[-1])))


    print("different diseases: " + str(df["diseases"].nunique()))
    # df = df[df["doid"].notnull()]

    print(df.head())
    #    patient_id                                      diseases  similarities  mondo          doid
    # 0    15013028                           depressive disorder      0.000054   2050     DOID:1596
    # 1    15013028                  benign blood vessel neoplasm      0.000012  24286    DOID:60006
    # 2    15013028  autosomal recessive nonsyndromic deafness 53      0.000054  12333  DOID:0110509
    
    print("length of df: " + str(len(df)))
    # filter for doid not Nan
    df = df[df["doid"].notnull()]
    print("length of df after filtering: " + str(len(df)))

    disease_patients_map = get_disease_patient_map(df)
    print("Disease Patients Map: ", len(disease_patients_map))
    print("First Disease Patients Map: ", {k: v for k, v in list(disease_patients_map.items())[:5]})

    # group by patient_id
    grouped = df.groupby("patient_id")

    patient_sim_map = {}
    max_k = 20
    different_diseases = []
    for patient_id, group in grouped:
        group = group.sort_values(by="similarities", ascending=False)
        # add first k diseases to different diseases
        different_diseases.append(group["doid"].values[:max_k])
        # test_doid = "110761"
        # index_of_test_doid = group[group["doid"] == test_doid].index
        # print("Index of test doid: ", index_of_test_doid)
        # print("Length of group: ", len(group), " for patient: ", patient_id)
        for k in range(1, max_k + 1):
            overlap_score, overlap_score_random = get_disease_similarity_scores(
                patient_id, group, disease_patients_map, k
            )
            if patient_id not in patient_sim_map:
                patient_sim_map[patient_id] = {}
            patient_sim_map[patient_id][k] = {
                "overlap_score": overlap_score,
                "overlap_score_random": overlap_score_random,
            }

    number_of_patients = len(patient_sim_map)
    different_diseases = list(set([item for sublist in different_diseases for item in sublist]))
    print("Different Diseases in top 20: ", len(different_diseases))
    # Plot the average overlap vs K
    plot_disease_similarity_avg(patient_sim_map, max_k, file_name, number_of_patients)

    return


def get_disease_similarity_scores(patient_id, group, disease_patients_map, k=5):
    index = k - 1
    # print("group: ", group)
    candidate_disease_id = group.iloc[index]["doid"]
    stripped_disease_id = candidate_disease_id.split(":")[-1]
    stripped_disease_id = str(int(stripped_disease_id))
    if len(group) < k:
        print(f"Patient {patient_id} has less than {k} diseases")
        return 0, 0
    if stripped_disease_id not in disease_patients_map.keys():
        # print(f"Disease {stripped_disease_id} has no patients")
        return 0, 0

    overlap_score = 1 if patient_id in disease_patients_map[stripped_disease_id] else 0

    random_dec = random.randint(0, len(disease_patients_map) - 1)
    overlap_score_random = 1 if random_dec == 1 else 0

    return overlap_score, overlap_score_random


def plot_disease_similarity_avg(
    patient_sim_map, k_max, score_file_path, number_of_patient
):
    k_values = range(1, k_max + 1)

    k_overlap_total = {k: 0 for k in k_values}
    k_overlap_random_total = {k: 0 for k in k_values}

    for patient_id in patient_sim_map:
        for k in k_values:
            k_overlap_total[k] += patient_sim_map[patient_id][k]["overlap_score"]
            k_overlap_random_total[k] += patient_sim_map[patient_id][k][
                "overlap_score_random"
            ]

    k_overlap_avg = [k_overlap_total[k] / number_of_patient for k in k_values]
    k_overlap_random_avg = [
        k_overlap_random_total[k] / number_of_patient for k in k_values
    ]

    k_overlap_cumsum = []
    k_overlap_random_cumsum = []
    cum_sum = 0
    cum_sum_random = 0
    for i in range(len(k_values)):
        cum_sum += k_overlap_avg[i]
        cum_sum_random += k_overlap_random_avg[i]
        k_overlap_cumsum.append(cum_sum)
        k_overlap_random_cumsum.append(cum_sum_random)

    plt.figure(figsize=(8, 6))
    # Define colors for each metric
    color1 = 'blue'
    color2 = 'red'
    plt.plot(k_values, k_overlap_avg, label="Patients has disease", color=color1)
    plt.plot(k_values, k_overlap_random_avg, label="Random Baseline", color=color1, linestyle="--")
    plt.plot(k_values, k_overlap_cumsum, label="Patients has disease aggregated", color=color2)
    plt.plot(k_values, k_overlap_random_cumsum, label="Random Baseline aggregated", color=color2, linestyle="--")

    plt.xlabel("Top-K Similar Diseases")
    plt.ylabel("Has disease avgerage")
    plt.title("Disease Characterization: Patient has disease at position k")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    out_file = (
        project_config.PROJECT_DIR / "plots" / "disease_characterization_scores.png"
    )
    print(f"Saving plot to {out_file}")
    plt.savefig(out_file)
    plt.close()
    print("Last aggregated Value: ", k_overlap_cumsum[-1])


def create_names_to_doid_map(disease_names):
    driver = utils.connect_to_neo4j()
    base_query = """
    WITH $clean_name AS input
    MATCH (d:Disease)
    WHERE apoc.text.levenshteinDistance(input, d.name) < 10
    RETURN d.id, apoc.text.levenshteinDistance(input, d.name) AS distance
    ORDER BY distance ASC
    LIMIT 1
    """
    name_id_map = {}
    for disease in tqdm(disease_names):
        clean_name = disease.replace("'", "").replace('"', "")
        params = {"clean_name": clean_name}
        res = utils.execute_query(driver, base_query, params, debug=False)
        # print(f"Disease: {clean_name}, Result: {res}")
        # print(f"Result: {res}")
        if len(res) > 0:
            name_id_map[clean_name] = res[0]["d.id"]
        # else:
        # print(f"No result for {clean_name}")

    print("Name to DOID Map: ", len(name_id_map))
    return name_id_map


def create_syn_names_to_doid_map(disease_names):
    driver = utils.connect_to_neo4j()
    base_query = """
    WITH $clean_name AS input
    MATCH (d:Disease)
    WHERE any(syn IN d.synonyms WHERE apoc.text.levenshteinDistance(input, syn) < 10)
    RETURN d.id
    """
    syn_name_id_map = {}
    for disease in tqdm(disease_names):
        clean_name = disease.replace("'", "").replace('"', "")
        params = {"clean_name": clean_name}
        res = utils.execute_query(driver, base_query, params, debug=False)
        if len(res) > 0:
            syn_name_id_map[clean_name] = res[0]["d.id"]

    print("Synonym Name to DOID Map: ", len(syn_name_id_map))
    return syn_name_id_map


def create_diseases_names_file(score_file_path, save_file):
    df = pd.read_csv(score_file_path)
    disease_names = df["diseases"].unique()
    print("Unique Diseases: ", len(disease_names))
    df.to_csv(save_file, index=False)
    print(f"Saved disease names to {save_file}")
    return df


def test_disease_mappings(score_file_path):
    diseases_mapping_dir = project_config.PROJECT_DIR / "disease_mappings"
    diseases_file = diseases_mapping_dir / "disease_names.csv"
    if not diseases_file.exists():
        df = create_diseases_names_file(score_file_path, save_file=diseases_file)
    else:
        df = pd.read_csv(diseases_file)

    disease_names = df["diseases"].unique()

    mondo_to_doid_dict = get_mondo_to_doid_dict()
    print("First mondo: ", {k: v for k, v in list(mondo_to_doid_dict.items())[:5]})

    db_name_to_doid_dict = get_db_names_to_doid_dict(disease_names)
    print("First db name: ", {k: v for k, v in list(db_name_to_doid_dict.items())[:5]})

    db_syn_names_to_doid_dict = get_db_syn_names_to_doid_dict(disease_names)
    print(
        "First db syn name: ",
        {k: v for k, v in list(db_syn_names_to_doid_dict.items())[:5]},
    )

    name_to_hpo_dict = get_name_to_hpo_dict()
    print(
        "First name_to_hpo_dict: ",
        {k: v for k, v in list(name_to_hpo_dict.items())[:5]},
    )

    name_to_mondo_dict = get_name_to_mondo_dict()
    print(
        "First name_to_mondo_dict: ",
        {k: v for k, v in list(name_to_mondo_dict.items())[:5]},
    )

    mondo_id_to_doid_dict = get_mondo_id_to_doid_dict()
    print(
        "First mondo_id_to_doid_dict: ",
        {k: v for k, v in list(mondo_id_to_doid_dict.items())[:5]},
    )

    total_diseases = len(disease_names)
    total_diseases_in_mondo = df[df["diseases"].isin(mondo_to_doid_dict.keys())][
        "diseases"
    ].nunique()
    total_diseases_in_db = df[df["diseases"].isin(db_name_to_doid_dict.keys())][
        "diseases"
    ].nunique()
    total_diseases_in_db_syn = df[
        df["diseases"].isin(db_syn_names_to_doid_dict.keys())
    ]["diseases"].nunique()
    total_diseases_in_hpo = df[df["diseases"].isin(name_to_hpo_dict.keys())][
        "diseases"
    ].nunique()
    total_diseases_in_mondo_name = df[df["diseases"].isin(name_to_mondo_dict.keys())][
        "diseases"
    ].nunique()

    # first map using the mondo to name dict then from mondo to doid
    df["mondo_id"] = df["diseases"].map(name_to_mondo_dict)
    # Mondo auf 7 stellen auffüllen und MONDO: davor setzen
    df["mondo_id"] = df["mondo_id"].apply(lambda x: f"MONDO:{str(x).zfill(7)}")
    df["doid"] = df["mondo_id"].map(mondo_id_to_doid_dict)
    total_diseases_mondo_name_mondo_id_doid = df[df["doid"].notnull()][
        "diseases"
    ].nunique()

    print(
        f"""Total Diseases: {total_diseases}, Total Diseases in Mondo: {total_diseases_in_mondo}, 
        Total Diseases in DB: {total_diseases_in_db}, Total Diseases in DB Syn: {total_diseases_in_db_syn}, 
        Total Diseases in HPO: {total_diseases_in_hpo}, Total Diseases in Mondo Name: {total_diseases_in_mondo_name}
        Total Diseases in Mondo Name to Mondo ID to DOID: {total_diseases_mondo_name_mondo_id_doid}
"""
    )

    # check overlap
    overlap_mondo_db = len(
        set(mondo_to_doid_dict.keys()).intersection(set(db_name_to_doid_dict.keys()))
    )
    overlap_mondo_db_syn = len(
        set(mondo_to_doid_dict.keys()).intersection(
            set(db_syn_names_to_doid_dict.keys())
        )
    )
    overlap_db_db_syn = len(
        set(db_name_to_doid_dict.keys()).intersection(
            set(db_syn_names_to_doid_dict.keys())
        )
    )
    print(
        f"Overlap Mondo and DB: {overlap_mondo_db}, Overlap Mondo and DB Syn: {overlap_mondo_db_syn}, Overlap DB and DB Syn: {overlap_db_db_syn}"
    )


def get_mondo_name_to_doid_dict():
    mondo_name_to_mondo_dict = get_name_to_mondo_dict()
    mondo_id_to_doid_dict = get_mondo_id_to_doid_dict()
    mondo_name_to_doid_dict = {
        k: mondo_id_to_doid_dict[f"MONDO:{str(v).zfill(7)}"]
        for k, v in mondo_name_to_mondo_dict.items()
        if f"MONDO:{str(v).zfill(7)}" in mondo_id_to_doid_dict
    }
    return mondo_name_to_doid_dict


def get_mondo_to_doid_dict():
    file_name = project_config.PROJECT_DIR / "mondo_to_doid_dict.pkl"
    if file_name.exists():
        with open(file_name, "rb") as handle:
            mondo_to_doid_dict = pickle.load(handle)
    else:
        mondo_to_doid_dict = project_utils.get_mondo_to_doid_dict()
        with open(file_name, "wb") as handle:
            pickle.dump(mondo_to_doid_dict, handle)
    return mondo_to_doid_dict


def get_db_names_to_doid_dict(disease_names):
    file_name = project_config.PROJECT_DIR / "db_name_to_doid_dict.pkl"
    if file_name.exists():
        with open(file_name, "rb") as handle:
            db_name_to_doid_dict = pickle.load(handle)
    else:
        db_name_to_doid_dict = create_names_to_doid_map(disease_names)
        with open(file_name, "wb") as handle:
            pickle.dump(db_name_to_doid_dict, handle)
    return db_name_to_doid_dict


def get_name_to_hpo_dict():
    file = (
        project_config.PROJECT_DIR
        / "knowledge_graph"
        / "8.9.21_kg"
        / f"hpo_to_name_dict_8.9.21_kg.pkl"
    )
    with open(file, "rb") as handle:
        hpo_to_name_dict = pickle.load(handle)
    name_to_hpo = {v: k for k, v in hpo_to_name_dict.items()}
    return name_to_hpo


def get_name_to_mondo_dict():
    file = (
        project_config.PROJECT_DIR
        / "knowledge_graph"
        / "8.9.21_kg"
        / f"mondo_to_name_dict_8.9.21_kg.pkl"
    )
    with open(file, "rb") as handle:
        mondo_to_name_dict = pickle.load(handle)
    name_to_mondo = {v: k for k, v in mondo_to_name_dict.items()}
    return name_to_mondo


def get_mondo_id_to_doid_dict():
    file = project_config.PROJECT_DIR / "mondo_id_to_doid_dict.pkl"
    if file.exists():
        with open(file, "rb") as handle:
            mondo_id_to_doid_dict = pickle.load(handle)
    else:
        mondo_id_to_doid_dict = create_mondo_id_to_doid_map()
        with open(file, "wb") as handle:
            pickle.dump(mondo_id_to_doid_dict, handle)
    return mondo_id_to_doid_dict


def create_mondo_id_to_doid_map():
    mondo_ontology = Ontology(project_config.PROJECT_DIR / "mondo.obo")
    mondo_rare_ontology = Ontology(project_config.PROJECT_DIR / "mondo-rare.obo")
    mondo_to_doid_dict = {}
    print("Creating mondo to DOID dict")
    for term in mondo_ontology.terms():
        if term.id.startswith("MONDO:"):
            for xref in term.xrefs:
                if xref.id.startswith("DOID:"):
                    mondo_to_doid_dict[term.id] = xref.id
                    break

    print("len mondo_to_doid_dict: ", len(mondo_to_doid_dict))

    for term in mondo_rare_ontology.terms():
        if term.id.startswith("MONDO:"):
            for xref in term.xrefs:
                if xref.id.startswith("DOID:"):
                    mondo_to_doid_dict[term.id] = xref.id
                    break

    print("len after rare dis: ", len(mondo_to_doid_dict))

    return mondo_to_doid_dict


def get_db_syn_names_to_doid_dict(disease_names):
    file_name = project_config.PROJECT_DIR / "db_syn_name_to_doid_dict.pkl"
    if file_name.exists():
        with open(file_name, "rb") as handle:
            db_syn_name_to_doid_dict = pickle.load(handle)
    else:
        db_syn_name_to_doid_dict = create_syn_names_to_doid_map(disease_names)
        with open(file_name, "wb") as handle:
            pickle.dump(db_syn_name_to_doid_dict, handle)
    return db_syn_name_to_doid_dict


if __name__ == "__main__":
    ### EXCLUDE CONTROL DISEASE?? ###
    agg_type = "phen"
    base_res = "checkpoints.patients_like_me_scores"
    dir = project_config.PROJECT_DIR / "results"
    file = dir / f"{base_res}_{agg_type}_primeKG_w_dis.csv"

    # evaluate_patients_like_me(file, min_dis_count=1)
    # evaluate_patients_like_me(file, min_dis_count=3)
    # evaluate_patients_like_me(file, min_dis_count=10)

    disease_char_file = (
        dir / "checkpoints.disease_characterization_hauner_scores_10.csv"
    )
    evaluate_disease_characterization(disease_char_file,)
    # evaluate_patients_like_me("SHEPHERD/data/results_with_genes/checkpoints.patients_like_me_scores.csv")
    # test_disease_mappings(disease_char_file)
# %%
