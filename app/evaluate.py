#%%
import pandas as pd
import utils as utils
import matplotlib.pyplot as plt
from app.SHEPHERD import project_config


def evaluate_patients_like_me(score_file_path):
    df = pd.read_csv(score_file_path)

    

    patients_disease_map = get_all_patients_diseases(df)

    patients_with_disease = [k for k, v in patients_disease_map.items() if len(v["diseases"]) > 0]
    print(f"Patients with diseases: {len(patients_with_disease)}")

    # filtered_df = df.filter(lambda x: x["patient_id"] in patients_with_disease)

    df = df.groupby("patient_id")
    print(df.head())

    patient_sim_map = {}
    max_k = 10
    for patient_id, group in df:
        for k in range(1, max_k+1):
            id_similar, icd10_similar = get_patient_similarity_scores(patient_id, group, patients_disease_map,k=k)
            if patient_id not in patient_sim_map:
                patient_sim_map[patient_id] = {}
            patient_sim_map[patient_id][k] = {"id_similar": id_similar, "icd10_similar": icd10_similar}

    plot_patient_similarity_avg(patient_sim_map, max_k, score_file_path)

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

def plot_patient_similarity_avg(patient_sim_map,k_max, score_file_path):
    patient_ids = list(patient_sim_map.keys())
    k_values = range(1,  k_max+1)

    len_patient_ids = len(patient_ids)
    k_icd10_similar_total = {k: 0 for k in k_values}
    k_id_similar_total = {k: 0 for k in k_values}

    for patient_id in patient_ids:
        for k in k_values:
            k_id_similar_total[k] += patient_sim_map[patient_id][k]["id_similar"]
            k_icd10_similar_total[k] += patient_sim_map[patient_id][k]["icd10_similar"]
    
    k_id_similar_avg = {k: k_id_similar_total[k]/k for k in k_values}
    k_icd10_similar_avg = {k: k_icd10_similar_total[k]/k for k in k_values}

    fig, ax = plt.subplots()
    ax.plot(k_values, list(k_id_similar_avg.values()), label="ID Similar")
    ax.plot(k_values, list(k_icd10_similar_avg.values()), label="ICD10 Similar")
    ax.set_xlabel("K")
    ax.set_ylabel("Similarity")
    ax.set_title("Patient Similarity Average of k highest scored patients.\n At least one similar disease \n File: " + str(score_file_path))
    ax.legend()
    file = project_config.PROJECT_DIR / "plots" / f"patient_similarity_scores.png"
    print(f"Saving plot to {file}")
    plt.savefig(file)


def get_patient_similarity_scores(patient_id, group, patients_disease_map, k=5):
    if(patient_id not in patients_disease_map):
        print(f"Patient {patient_id} has no diseases")
        return 0, 0
    patient_disease = patients_disease_map[patient_id]
    id_similar = 0
    icd10_similar = 0
    index= 0
    # sort group by score
    group = group.sort_values(by="similarities", ascending=False)

    count = 0
    for i, row in group.iterrows():
        candidate_patient_id = int(row["candidate_patients"])
        if(candidate_patient_id not in patients_disease_map):
            count += 1
            continue
        candidate_patient_disease = patients_disease_map[candidate_patient_id]
        id_similarity_set =set(patient_disease["diseases"]).intersection(set(candidate_patient_disease["diseases"]))
        icd10_similarity_set = set(patient_disease["icd10_codes"]).intersection(set(candidate_patient_disease["icd10_codes"]))
        
        # if len(id_similarity_set) > 0:
        #     print(f"Patient {patient_id} and Patient {candidate_patient_id} have similar diseases: {id_similarity_set}")
        # if len(icd10_similarity_set) > 0:
        #     print(f"Patient {patient_id} and Patient {candidate_patient_id} have similar icd10 codes: {icd10_similarity_set}")

        id_similar += len(id_similarity_set) > 0
        icd10_similar += len(icd10_similarity_set) > 0
        if index == k:
            break
        index += 1
    # print(f"Patient {patient_id} has {count} patients without diseases")
    return id_similar, icd10_similar
    
def get_all_patients_diseases(df):
    driver = utils.connect_to_neo4j()
    patient_ids = df["patient_id"].unique()
    candidate_patients = df["candidate_patients"].unique()
    all_patient_ids = list(patient_ids) + list(candidate_patients)
    print("Head: ", all_patient_ids[:5])
    all_patient_ids = [x[0] for x in all_patient_ids]
    unique_patient_ids = list(set(all_patient_ids))


    query = f"""
    MATCH (p:Biological_sample)-[:HAS_DISEASE]->(d:Disease)
    WHERE id(p) in {unique_patient_ids}
    RETURN id(p) as patient_id, collect(id(d)) as diseases, collect([syn IN d.synonyms WHERE syn STARTS WITH "ICD10"] )AS icd10_codes

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
        patient_disease_map[patient_id] = {"diseases": diseases, "icd10_codes": icd10_codes}
    
    return patient_disease_map




    


if __name__ == "__main__":
    ### EXCLUDE CONTROL DISEASE?? ###
    agg_type = "phen"
    base_res = "checkpoints.patients_like_me_scores"
    dir = project_config.PROJECT_DIR / "results" 
    file = dir / f"{base_res}_{agg_type}_primeKG_w_dis.csv"
    print(f"Evalute: {file}")
    evaluate_patients_like_me(file)
    # evaluate_patients_like_me("SHEPHERD/data/results_with_genes/checkpoints.patients_like_me_scores.csv")
# %%
