# %%
import pandas as pd
import utils as utils
import matplotlib.pyplot as plt
from app.SHEPHERD import project_config
import random
import pickle
import sys

from app.SHEPHERD import project_utils

def evaluate_patients_like_me(score_file_path):
    print(f"Evalute Patients Like me: {file}")
    df = pd.read_csv(score_file_path)

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
        patient_sim_map, max_k, score_file_path, number_of_patients=number_of_patients
    )


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
    patient_sim_map, k_max, score_file_path, number_of_patients
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
            k_icd10_first_4_similar_total[k] += patient_sim_map[patient_id][k]["icd10_first_4_similarity_set"]
            k_icd10_first_4_similar_random_total[k] += patient_sim_map[patient_id][k]["icd10_first_4_similarity_set_random"]

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
        k: k_icd10_first_4_similar_random_total[k] / number_of_patients for k in k_values
    }

    fig, ax = plt.subplots()
    ax.plot(k_values, list(k_id_similar_avg.values()), label="ID Similar")
    ax.plot(k_values, list(k_icd10_similar_avg.values()), label="ICD10 Similar")
    ax.plot(k_values, list(k_id_similar_random_avg.values()), label="ID Similar Random")
    ax.plot(
        k_values,
        list(k_icd10_similar_random_avg.values()),
        label="ICD10 Similar Random",
    )
    ax.plot(
        k_values,
        list(k_icd10_first_4_similar_avg.values()),
        label="ICD10 First 5 Similar",
    )
    ax.plot(
        k_values,
        list(k_icd10_first_4_similar_random_avg.values()),
        label="ICD10 First 5 Similar Random",
    )
    ax.set_xlabel("K")
    ax.set_ylabel("Similarity")
    ax.set_title(
        "Patient Similarity Average of patient at rank k.\n At least one similar disease or icd10 code"
    )
    ax.legend()
    file = project_config.PROJECT_DIR / "plots" / f"patient_similarity_scores.png"
    print(f"Saving plot to {file}")
    plt.savefig(file)


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
    ).intersection(
        set(code[:10] for code in candidate_patient_disease["icd10_codes"])
    )

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
    ).intersection(
        set(code[:10] for code in random_patient_disease["icd10_codes"]))

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
        icd10_first_4_similarity_random
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


def map_disease_to_doid(df):
    mondo_to_name_dict_file = utils.SHEPHERD_DIR + f"/data_prep/mondo_to_name_dict_8.9.21_kg.pkl"
    mondo_to_name_dict = pickle.load(open(mondo_to_name_dict_file, "rb"))
    name_to_mondo_dict = {v: k for k, v in mondo_to_name_dict.items()}
    mondo_to_doid_dict = project_utils.get_mondo_to_doid_dict()
    # mondo_to_ICD10_dict = project_utils.get_mondo_to_ICD10_dict()
    # print("First 5 diseases: ", list(mondo_to_ICD10_dict.items())[:5])
    # remove "MONDO:" from keys
    mondo_to_doid_dict = {k[6:].lstrip("0"): v for k, v in mondo_to_doid_dict.items()}
   
    # map df disease from disease to doid
    df["mondo"] = df["diseases"].map(name_to_mondo_dict)
    df["doid"] = df["mondo"].map(mondo_to_doid_dict)
    return df


def get_disease_patient_map(df):
    driver = utils.connect_to_neo4j()
    patient_ids = df["patient_id"].unique()

    diseases = df["doid"].unique()

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
        if disease_id not in disease_patient_map:
            disease_patient_map[disease_id] = set()
        disease_patient_map[disease_id].add(patient_id)
    return disease_patient_map



def evaluate_disease_characterization(file_name,):
    df = pd.read_csv(file_name)
    print(df.head())
    
    df = map_disease_to_doid(df)

    print("Total lenght: ", len(df))
    print("Not found DOID: " + str(df["doid"].isnull().sum()))
    df = df[df["doid"].notnull()]

    print(df.head())
    #    patient_id                                      diseases  similarities  mondo          doid
    # 0    15013028                           depressive disorder      0.000054   2050     DOID:1596
    # 1    15013028                  benign blood vessel neoplasm      0.000012  24286    DOID:60006
    # 2    15013028  autosomal recessive nonsyndromic deafness 53      0.000054  12333  DOID:0110509


    disease_patients_map = get_disease_patient_map(df)
    # group by patient_id
    grouped = df.groupby("doid")
    
    disease_sim_map = {}
    max_k = 10  # or whatever top K range you want
    for disease_id, group in grouped:
        # We'll compute overlap for k=1..max_k
        for k in range(1, max_k + 1):
            overlap_score, overlap_score_random = get_disease_similarity_scores(
                disease_id, group, disease_patients_map, k
            )
            if disease_id not in disease_sim_map:
                disease_sim_map[disease_id] = {}
            disease_sim_map[disease_id][k] = {
                "overlap_score": overlap_score,
                "overlap_score_random": overlap_score_random,
            }
    
    number_of_diseases = len(disease_sim_map)
    
    # Plot the average overlap vs K
    plot_disease_similarity_avg(
        disease_sim_map, max_k, file_name, number_of_diseases
    )


    return


def get_disease_similarity_scores(disease_id, group, disease_patients_map, k=5):
    if disease_id not in disease_patients_map:
        return 0, 0
    group_sorted = group.sort_values(by="similarities", ascending=False)
    if len(group_sorted) < k:
        return 0, 0
    candidate_disease_id = group_sorted.iloc[k - 1]["doid"]  
    if candidate_disease_id not in disease_patients_map:
        return 0, 0
    overlap = disease_patients_map[disease_id].intersection(
        disease_patients_map[candidate_disease_id]
    )
    overlap_score = 1 if len(overlap) > 0 else 0
    
    random_disease_id = random.choice(list(disease_patients_map.keys()))
    random_overlap = disease_patients_map[disease_id].intersection(
        disease_patients_map[random_disease_id]
    )
    overlap_score_random = 1 if len(random_overlap) > 0 else 0
    
    return overlap_score, overlap_score_random



def plot_disease_similarity_avg(disease_sim_map, k_max, score_file_path, number_of_diseases):
    k_values = range(1, k_max + 1)
    
    k_overlap_total = {k: 0 for k in k_values}
    k_overlap_random_total = {k: 0 for k in k_values}
    
    for disease_id in disease_sim_map:
        for k in k_values:
            k_overlap_total[k] += disease_sim_map[disease_id][k]["overlap_score"]
            k_overlap_random_total[k] += disease_sim_map[disease_id][k]["overlap_score_random"]
    
    k_overlap_avg = [k_overlap_total[k] / number_of_diseases for k in k_values]
    k_overlap_random_avg = [k_overlap_random_total[k] / number_of_diseases for k in k_values]
    
    plt.figure(figsize=(8, 6))
    plt.plot(k_values, k_overlap_avg, label="Overlap in Patients")
    plt.plot(k_values, k_overlap_random_avg, label="Random Baseline")
    
    plt.xlabel("Top-K Similar Diseases")
    plt.ylabel("Fraction of Diseases with Overlap")
    plt.title("Disease Characterization: Average Overlap vs. K")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    out_file = project_config.PROJECT_DIR / "plots" / "disease_characterization_scores.png"
    print(f"Saving plot to {out_file}")
    plt.savefig(out_file)
    plt.close()


if __name__ == "__main__":
    ### EXCLUDE CONTROL DISEASE?? ###
    agg_type = "phen"
    base_res = "checkpoints.patients_like_me_scores"
    dir = project_config.PROJECT_DIR / "results"
    file = dir / f"{base_res}_{agg_type}_primeKG_w_dis.csv"
    
    # evaluate_patients_like_me(file)

    disease_char_file = (
        dir / "checkpoints.disease_characterization_scores_phen_primeKG_w_dis.csv"
    )
    evaluate_disease_characterization(disease_char_file,)
    # evaluate_patients_like_me("SHEPHERD/data/results_with_genes/checkpoints.patients_like_me_scores.csv")
# %%
