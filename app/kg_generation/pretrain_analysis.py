#%%
import matplotlib.pyplot as plt
results = {'edge_metrics/node.Biological_process;HAS_PARENT;Biological_process_test_acc': 0.49758830666542053,
 'edge_metrics/node.Biological_process;HAS_PARENT;Biological_process_test_ap': 0.517388105392456,
 'edge_metrics/node.Biological_process;HAS_PARENT;Biological_process_test_f1': 0.49758830666542053,
 'edge_metrics/node.Biological_process;HAS_PARENT;Biological_process_test_roc': 0.5020951628684998,
 'edge_metrics/node.Cellular_component;HAS_PARENT;Cellular_component_test_acc': 0.5167606472969055,
 'edge_metrics/node.Cellular_component;HAS_PARENT;Cellular_component_test_ap': 0.5894542932510376,
 'edge_metrics/node.Cellular_component;HAS_PARENT;Cellular_component_test_f1': 0.5167606472969055,
 'edge_metrics/node.Cellular_component;HAS_PARENT;Cellular_component_test_roc': 0.5484552979469299,
 'edge_metrics/node.Disease;HAS_PARENT;Disease_test_acc': 0.48280230164527893,
 'edge_metrics/node.Disease;HAS_PARENT;Disease_test_ap': 0.5376255512237549,
 'edge_metrics/node.Disease;HAS_PARENT;Disease_test_f1': 0.48280230164527893,
 'edge_metrics/node.Disease;HAS_PARENT;Disease_test_roc': 0.4699345529079437,
 'edge_metrics/node.Functional_region;FOUND_IN_PROTEIN;Protein_test_acc': 0.6379647850990295,
 'edge_metrics/node.Functional_region;FOUND_IN_PROTEIN;Protein_test_ap': 0.6759823560714722,
 'edge_metrics/node.Functional_region;FOUND_IN_PROTEIN;Protein_test_f1': 0.6379647850990295,
 'edge_metrics/node.Functional_region;FOUND_IN_PROTEIN;Protein_test_roc': 0.6852625012397766,
 'edge_metrics/node.Gene;ASSOCIATED_WITH;Disease_test_acc': 0.5016310811042786,
 'edge_metrics/node.Gene;ASSOCIATED_WITH;Disease_test_ap': 0.512111246585846,
 'edge_metrics/node.Gene;ASSOCIATED_WITH;Disease_test_f1': 0.5016310811042786,
 'edge_metrics/node.Gene;ASSOCIATED_WITH;Disease_test_roc': 0.4929749369621277,
 'edge_metrics/node.Gene;TRANSLATED_INTO;Protein_test_acc': 0.5905039310455322,
 'edge_metrics/node.Gene;TRANSLATED_INTO;Protein_test_ap': 0.6250561475753784,
 'edge_metrics/node.Gene;TRANSLATED_INTO;Protein_test_f1': 0.5905039310455322,
 'edge_metrics/node.Gene;TRANSLATED_INTO;Protein_test_roc': 0.6092648506164551,
 'edge_metrics/node.Molecular_function;HAS_PARENT;Molecular_function_test_acc': 0.5077763199806213,
 'edge_metrics/node.Molecular_function;HAS_PARENT;Molecular_function_test_ap': 0.5394691824913025,
 'edge_metrics/node.Molecular_function;HAS_PARENT;Molecular_function_test_f1': 0.5077763199806213,
 'edge_metrics/node.Molecular_function;HAS_PARENT;Molecular_function_test_roc': 0.5139120817184448,
 'edge_metrics/node.Phenotype;HAS_PARENT;Phenotype_test_acc': 0.5080164074897766,
 'edge_metrics/node.Phenotype;HAS_PARENT;Phenotype_test_ap': 0.5140474438667297,
 'edge_metrics/node.Phenotype;HAS_PARENT;Phenotype_test_f1': 0.5080164074897766,
 'edge_metrics/node.Phenotype;HAS_PARENT;Phenotype_test_roc': 0.5080366134643555,
 'edge_metrics/node.Phenotype;LINKED_VIA_D_TO;Gene_test_acc': 0.4988304674625397,
 'edge_metrics/node.Phenotype;LINKED_VIA_D_TO;Gene_test_ap': 0.5178245902061462,
 'edge_metrics/node.Phenotype;LINKED_VIA_D_TO;Gene_test_f1': 0.4988304674625397,
 'edge_metrics/node.Phenotype;LINKED_VIA_D_TO;Gene_test_roc': 0.4984159469604492,
 'edge_metrics/node.Phenotype;MAPS_TO;Disease_test_acc': 0.5055555701255798,
 'edge_metrics/node.Phenotype;MAPS_TO;Disease_test_ap': 0.5377777218818665,
 'edge_metrics/node.Phenotype;MAPS_TO;Disease_test_f1': 0.5055555701255798,
 'edge_metrics/node.Phenotype;MAPS_TO;Disease_test_roc': 0.5020370483398438,
 'edge_metrics/node.Protein;ACTS_ON;Protein_test_acc': 0.49952295422554016,
 'edge_metrics/node.Protein;ACTS_ON;Protein_test_ap': 0.5269123911857605,
 'edge_metrics/node.Protein;ACTS_ON;Protein_test_f1': 0.49952295422554016,
 'edge_metrics/node.Protein;ACTS_ON;Protein_test_roc': 0.4922817051410675,
 'edge_metrics/node.Protein;ANNOTATED_IN_PATHWAY;Pathway_test_acc': 0.6047604084014893,
 'edge_metrics/node.Protein;ANNOTATED_IN_PATHWAY;Pathway_test_ap': 0.5810246467590332,
 'edge_metrics/node.Protein;ANNOTATED_IN_PATHWAY;Pathway_test_f1': 0.6047604084014893,
 'edge_metrics/node.Protein;ANNOTATED_IN_PATHWAY;Pathway_test_roc': 0.5960370302200317,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Biological_process_test_acc': 0.4987853467464447,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Biological_process_test_ap': 0.5489031076431274,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Biological_process_test_f1': 0.4987853467464447,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Biological_process_test_roc': 0.510718822479248,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Cellular_component_test_acc': 0.4981282949447632,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Cellular_component_test_ap': 0.5216107964515686,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Cellular_component_test_f1': 0.4981282949447632,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Cellular_component_test_roc': 0.5041750073432922,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Disease_test_acc': 0.5010572671890259,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Disease_test_ap': 0.5173351764678955,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Disease_test_f1': 0.5010572671890259,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Disease_test_roc': 0.5014398694038391,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Molecular_function_test_acc': 0.5086477398872375,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Molecular_function_test_ap': 0.5530610680580139,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Molecular_function_test_f1': 0.5086477398872375,
 'edge_metrics/node.Protein;ASSOCIATED_WITH;Molecular_function_test_roc': 0.4983421564102173,
 'edge_metrics/node.Protein;COMPILED_INTERACTS_WITH;Protein_test_acc': 0.5009433627128601,
 'edge_metrics/node.Protein;COMPILED_INTERACTS_WITH;Protein_test_ap': 0.5183253884315491,
 'edge_metrics/node.Protein;COMPILED_INTERACTS_WITH;Protein_test_f1': 0.5009433627128601,
 'edge_metrics/node.Protein;COMPILED_INTERACTS_WITH;Protein_test_roc': 0.5001038908958435,
 'edge_metrics/node.Protein;CURATED_INTERACTS_WITH;Protein_test_acc': 0.49642378091812134,
 'edge_metrics/node.Protein;CURATED_INTERACTS_WITH;Protein_test_ap': 0.5466722249984741,
 'edge_metrics/node.Protein;CURATED_INTERACTS_WITH;Protein_test_f1': 0.49642378091812134,
 'edge_metrics/node.Protein;CURATED_INTERACTS_WITH;Protein_test_roc': 0.4932936429977417,
 'edge_metrics/node.Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease_test_acc': 0.49998047947883606,
 'edge_metrics/node.Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease_test_ap': 0.5168232917785645,
 'edge_metrics/node.Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease_test_f1': 0.49998047947883606,
 'edge_metrics/node.Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease_test_roc': 0.5010090470314026,
 'node_curr_epoch': 399.0,
 'test/node_acc': 0.5589880347251892,
 'test/node_ap': 0.5657259821891785,
 'test/node_batch_loss': 0.8934274315834045,
 'test/node_f1': 0.5589880347251892,
 'test/node_roc': 0.5700045228004456,
 'test/node_total_acc': 0.5589882135391235,
 'test/node_total_ap': 0.565726101398468,
 'test/node_total_f1': 0.5589882135391235,
 'test/node_total_roc': 0.5700039863586426}

rel_count ={
  "VARIANT_IS_CLINICALLY_RELEVANT": 169,
  "DETECTED_IN_PATHOLOGY_SAMPLE": 1697248,
  "LINKED_VIA_D_TO": 7244703,
  "ACTS_ON": 988705,
  "VARIANT_FOUND_IN_GENE": 10638935,
  "CURATED_INTERACTS_WITH": 299188,
  "IS_SUBSTRATE_OF": 994,
  "ASSOCIATED_WITH": 31105535,
  "TRANSLATED_INTO": 374294,
  "BELONGS_TO_PROTEIN": 3629058,
  "PUBLISHED_IN": 3939,
  "LOCATED_IN": 335339,
  "ANNOTATED_IN_PATHWAY": 1203809,
  "HAS_PROTEIN": 40000,
  "HAS_DAMAGE": 1499,
  "HAS_PHENOTYPE": 1776,
  "MENTIONED_IN_PUBLICATION": 111109238,
  "IS_BIOMARKER_OF_DISEASE": 515,
  "IS_SUBUNIT_OF": 10968,
  "STUDIES_TRAIT": 9250,
  "HAS_MODIFIED_SITE": 21421,
  "HAS_MODIFICATION": 21407,
  "HAS_DISEASE": 1611,
  "VARIANT_FOUND_IN_CHROMOSOME": 10630108,
  "VARIANT_FOUND_IN_GWAS": 16128,
  "BELONGS_TO_SUBJECT": 100,
  "HAS_ENROLLED": 100,
  "VARIANT_FOUND_IN_PROTEIN": 26807293,
  "TRANSCRIBED_INTO": 258487,
  "COMPILED_INTERACTS_WITH": 1956612,
  "HAS_PARENT": 2731475,
  "CURATED_AFFECTS_INTERACTION_WITH": 10873,
  "FOUND_IN_PROTEIN": 204244,
  "MAPS_TO": 14339,
  "IS_QCMARKER_IN_TISSUE": 249
}


def analyze_results(results):
    edge_metrics = {}
    for key in results:
        if "edge_metrics" in key and "node"  in key and "test_f1" in key:
            rel = key.split('_test_f1')[0]
            rel = rel.split('.')[-1]
            edge_metrics[rel] = results[key]
    return edge_metrics

def plot_by_disease_or_not(edge_metrics):
    disease_metrics = {}
    not_disease_metrics = {}
    for key in edge_metrics:
        if "Disease" in key:
            disease_metrics[key] = edge_metrics[key]
        else:
            not_disease_metrics[key] = edge_metrics[key]

    fig, ax = plt.subplots()
    ax.bar(disease_metrics.keys(), disease_metrics.values(), label='Disease')
    ax.bar(not_disease_metrics.keys(), not_disease_metrics.values(), label='Not Disease')
    ax.legend()
    plt.xticks(rotation=90)
    plt.show()
    return disease_metrics, not_disease_metrics

def filter_by_value():
    threshold = 0.55
    filtered = {k: v for k, v in edge_metrics.items() if v > threshold}
    # plot the filtered results
    fig, ax = plt.subplots()
    ax.bar(filtered.keys(), filtered.values())
    plt.xticks(rotation=90)

    plt.show()
    return filtered

def filter_by_simatricall():
    symmetrical = {}
    not_symmetrical = {}
    for key in edge_metrics:
        split_key = key.split(';')
        first_relation = split_key[0]
        second_relation =  split_key[2]
        if first_relation == second_relation:
            symmetrical[key] = edge_metrics[key]
        else:
            not_symmetrical[key] = edge_metrics[key]

    fig, ax = plt.subplots()
    ax.bar(symmetrical.keys(), symmetrical.values(), label='Symmetrical')
    ax.bar(not_symmetrical.keys(), not_symmetrical.values(), label='Not Symmetrical')
    ax.legend()
    plt.xticks(rotation=90)
    plt.show()
    return symmetrical, not_symmetrical

def map_by_relationship_count():
    x_vals, y_vals = [], []
    for k, v in edge_metrics.items():
        parts = k.split(';')
        if len(parts) > 1 and parts[1] in rel_count:
            x_vals.append(rel_count[parts[1]])
            y_vals.append(v)
    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals)
    ax.set_xlabel("Count")
    ax.set_ylabel("Metric")
    plt.title("Relationship Count vs Edge Metric")
    plt.show()
    return x_vals, y_vals
    
    

if __name__ == "__main__":
    edge_metrics = analyze_results(results)
    # disease_metrics, not_disease_metrics = plot_by_disease_or_not(edge_metrics)
    # filter_by_value()
    # filter_by_simatricall()
    map_by_relationship_count()