# General
import numpy as np
import pandas as pd

# from typing import List, Optional, Tuple, NamedTuple, Union, Callable

# Pytorch
import torch
import torch.nn as nn
from torch_geometric.data import Data
from torch import Tensor

import sys

sys.path.insert(0, "app/SHEPHERD")
import project_config


def preprocess_graph(args):

    # Read in nodes & edges
    nodes = pd.read_csv(project_config.KG_DIR / args.node_map, sep="\t")
    edges = pd.read_csv(project_config.KG_DIR / args.edgelist, sep="\t")

    # Initialize edge index
    edge_index = torch.LongTensor(edges[["x_idx", "y_idx"]].values.T).contiguous()
    edge_attr = edges["full_relation"]

    # Convert edge attributes to idx
    edge_attr_list = [
        ## hauner_graph
        # "Disease;HAS_PARENT;Disease",
        # "Tissue;HAS_PARENT;Tissue",
        # "Biological_process;HAS_PARENT;Biological_process",
        # "Molecular_function;HAS_PARENT;Molecular_function",
        # "Cellular_component;HAS_PARENT;Cellular_component",
        # "Modification;HAS_PARENT;Modification",
        # "Gene;ASSOCIATED_WITH;Disease",
        # "Gene;LOCATED_IN;Chromosome",
        # "Gene;TRANSCRIBED_INTO;Transcript",
        # "Gene;TRANSLATED_INTO;Protein",
        # "Transcript;LOCATED_IN;Chromosome",
        # "Transcript;TRANSLATED_INTO;Protein",
        # "Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease",
        # "Protein;ASSOCIATED_WITH;Disease",
        # "Protein;ASSOCIATED_WITH;Tissue",
        # "Protein;ASSOCIATED_WITH;Biological_process",
        # "Protein;ASSOCIATED_WITH;Molecular_function",
        # "Protein;ASSOCIATED_WITH;Cellular_component",
        # "Protein;COMPILED_INTERACTS_WITH;Protein",
        # "Protein;ACTS_ON;Protein",
        # "Protein;CURATED_INTERACTS_WITH;Protein",
        # "Protein;HAS_MODIFIED_SITE;Modified_protein",
        # "Protein;ANNOTATED_IN_PATHWAY;Pathway",
        # "Protein;IS_SUBUNIT_OF;Complex",
        # "Protein;IS_BIOMARKER_OF_DISEASE;Disease",
        # "Protein;IS_QCMARKER_IN_TISSUE;Tissue",
        # "Peptide;BELONGS_TO_PROTEIN;Protein",
        # "Peptide;HAS_MODIFIED_SITE;Modified_protein",
        # "Modified_protein;HAS_MODIFICATION;Modification",
        # "Modified_protein;IS_SUBSTRATE_OF;Protein",
        # "Complex;ASSOCIATED_WITH;Biological_process",
        # "Known_variant;VARIANT_FOUND_IN_CHROMOSOME;Chromosome",
        # "Known_variant;VARIANT_FOUND_IN_GENE;Gene",
        # "Known_variant;VARIANT_FOUND_IN_PROTEIN;Protein",
        # "Known_variant;VARIANT_IS_CLINICALLY_RELEVA    # "Disease;HAS_PARENT;Disease",
        # "Tissue;HAS_PARENT;Tissue",
        # "Biological_process;HAS_PARENT;Biological_process",
        # "Molecular_function;HAS_PARENT;Molecular_function",
        # "Cellular_component;HAS_PARENT;Cellular_component",
        # "Modification;HAS_PARENT;Modification",
        # "Gene;ASSOCIATED_WITH;Disease",
        # "Gene;LOCATED_IN;Chromosome",
        # "Gene;TRANSCRIBED_INTO;Transcript",
        # "Gene;TRANSLATED_INTO;Protein",
        # "Transcript;LOCATED_IN;Chromosome",
        # "Transcript;TRANSLATED_INTO;Protein",
        # "Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease",
        # "Protein;ASSOCIATED_WITH;Disease",
        # "Protein;ASSOCIATED_WITH;Tissue",
        # "Protein;ASSOCIATED_WITH;Biological_process",
        # "Protein;ASSOCIATED_WITH;Molecular_function",
        # "Protein;ASSOCIATED_WITH;Cellular_component",
        # "Protein;COMPILED_INTERACTS_WITH;Protein",
        # "Protein;ACTS_ON;Protein",
        # "Protein;CURATED_INTERACTS_WITH;Protein",
        # "Protein;HAS_MODIFIED_SITE;Modified_protein",
        # "Protein;ANNOTATED_IN_PATHWAY;Pathway",
        # "Protein;IS_SUBUNIT_OF;Complex",
        # "Protein;IS_BIOMARKER_OF_DISEASE;Disease",
        # "Protein;IS_QCMARKER_IN_TISSUE;Tissue",
        # "Peptide;BELONGS_TO_PROTEIN;Protein",
        # "Peptide;HAS_MODIFIED_SITE;Modified_protein",
        # "Modified_protein;HAS_MODIFICATION;Modification",
        # "Modified_protein;IS_SUBSTRATE_OF;Protein",
        # "Complex;ASSOCIATED_WITH;Biological_process",
        # "Clinically_relevant_variant;ASSOCIATED_WITH;Disease",
        # "Functional_region;FOUND_IN_PROTEIN;Protein",
        # "Metabolite;ASSOCIATED_WITH;Disease",
        # "Metabolite;ANNOTATED_IN_PATHWAY;Pathway",
        # "Metabolite;ASSOCIATED_WITH;Protein",NT;Clinically_relevant_variant",
        # "Known_variant;CURATED_AFFECTS_INTERACTION_WITH;Protein",
        # "Clinically_relevant_variant;ASSOCIATED_WITH;Disease",
        # "Functional_region;FOUND_IN_PROTEIN;Protein",
        # "Metabolite;ASSOCIATED_WITH;Disease",
        # "Metabolite;ANNOTATED_IN_PATHWAY;Pathway",
        # "Metabolite;ASSOCIATED_WITH;Protein",
        ## hauner_graph_reduced
        # "Disease;HAS_PARENT;Disease",
        # "Tissue;HAS_PARENT;Tissue",
        # "Biological_process;HAS_PARENT;Biological_process",
        # "Molecular_function;HAS_PARENT;Molecular_function",
        # "Cellular_component;HAS_PARENT;Cellular_component",
        # "Modification;HAS_PARENT;Modification",
        # "Gene;ASSOCIATED_WITH;Disease",
        # "Gene;LOCATED_IN;Chromosome",
        # "Gene;TRANSCRIBED_INTO;Transcript",
        # "Gene;TRANSLATED_INTO;Protein",
        # "Transcript;LOCATED_IN;Chromosome",
        # "Transcript;TRANSLATED_INTO;Protein",
        # "Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease",
        # "Protein;ASSOCIATED_WITH;Disease",
        # "Protein;ASSOCIATED_WITH;Tissue",
        # "Protein;ASSOCIATED_WITH;Biological_process",
        # "Protein;ASSOCIATED_WITH;Molecular_function",
        # "Protein;ASSOCIATED_WITH;Cellular_component",
        # "Protein;COMPILED_INTERACTS_WITH;Protein",
        # "Protein;ACTS_ON;Protein",
        # "Protein;CURATED_INTERACTS_WITH;Protein",
        # "Protein;HAS_MODIFIED_SITE;Modified_protein",
        # "Protein;ANNOTATED_IN_PATHWAY;Pathway",
        # "Protein;IS_SUBUNIT_OF;Complex",
        # "Protein;IS_BIOMARKER_OF_DISEASE;Disease",
        # "Protein;IS_QCMARKER_IN_TISSUE;Tissue",
        # "Peptide;BELONGS_TO_PROTEIN;Protein",
        # "Peptide;HAS_MODIFIED_SITE;Modified_protein",
        # "Modified_protein;HAS_MODIFICATION;Modification",
        # "Modified_protein;IS_SUBSTRATE_OF;Protein",
        # "Complex;ASSOCIATED_WITH;Biological_process",
        # "Clinically_relevant_variant;ASSOCIATED_WITH;Disease",
        # "Functional_region;FOUND_IN_PROTEIN;Protein",
        # "Metabolite;ASSOCIATED_WITH;Disease",
        # "Metabolite;ANNOTATED_IN_PATHWAY;Pathway",
        # "Metabolite;ASSOCIATED_WITH;Protein",
        ## hauner_graph_reduced with only shepherd types
        "Disease;HAS_PARENT;Disease",
        "Biological_process;HAS_PARENT;Biological_process",
        "Molecular_function;HAS_PARENT;Molecular_function",
        "Cellular_component;HAS_PARENT;Cellular_component",
        "Phenotype;HAS_PARENT;Phenotype",
        "Phenotype;MAPS_TO;Disease",
        "Phenotype;LINKED_VIA_D_TO;Gene",
        "Gene;ASSOCIATED_WITH;Disease",
        "Gene;TRANSLATED_INTO;Protein",
        "Protein;DETECTED_IN_PATHOLOGY_SAMPLE;Disease",
        "Protein;ASSOCIATED_WITH;Disease",
        "Protein;ASSOCIATED_WITH;Biological_process",
        "Protein;ASSOCIATED_WITH;Molecular_function",
        "Protein;ASSOCIATED_WITH;Cellular_component",
        "Protein;COMPILED_INTERACTS_WITH;Protein",
        "Protein;ACTS_ON;Protein",
        "Protein;CURATED_INTERACTS_WITH;Protein",
        "Protein;ANNOTATED_IN_PATHWAY;Pathway",
        "Protein;IS_BIOMARKER_OF_DISEASE;Disease",
        "Functional_region;FOUND_IN_PROTEIN;Protein",
        ## 8.9.21_kg - old shepherd graph
        #   'effect/phenotype;phenotype_protein;gene/protein',
        #   'gene/protein;phenotype_protein;effect/phenotype',
        #   'disease;disease_phenotype_negative;effect/phenotype',
        #   'effect/phenotype;disease_phenotype_negative;disease',
        #   'disease;disease_phenotype_positive;effect/phenotype',
        #   'effect/phenotype;disease_phenotype_positive;disease',
        #   'gene/protein;protein_pathway;pathway',
        #   'pathway;protein_pathway;gene/protein',
        #   'disease;disease_protein;gene/protein',
        #   'gene/protein;disease_protein;disease',
        #   'gene/protein;protein_molfunc;molecular_function',
        #   'molecular_function;protein_molfunc;gene/protein',
        #   'gene/protein;protein_cellcomp;cellular_component',
        #   'cellular_component;protein_cellcomp;gene/protein',
        #   'gene/protein;protein_bioprocess;biological_process',
        #   'biological_process;protein_bioprocess;gene/protein',
        #   'biological_process;bioprocess_bioprocess;biological_process',
        #   'biological_process;bioprocess_bioprocess_rev;biological_process',
        #   'molecular_function;molfunc_molfunc;molecular_function',
        #   'molecular_function;molfunc_molfunc_rev;molecular_function',
        #   'cellular_component;cellcomp_cellcomp;cellular_component',
        #   'cellular_component;cellcomp_cellcomp_rev;cellular_component',
        #   'effect/phenotype;phenotype_phenotype;effect/phenotype',
        #   'effect/phenotype;phenotype_phenotype_rev;effect/phenotype',
        #   'gene/protein;protein_protein;gene/protein',
        #   'gene/protein;protein_protein_rev;gene/protein',
        #   'disease;disease_disease;disease',
        #   'disease;disease_disease_rev;disease',
        #   'pathway;pathway_pathway;pathway',
        #   'pathway;pathway_pathway_rev;pathway'
    ]

    edge_attr_to_idx_dict = {attr: i for i, attr in enumerate(edge_attr_list)}
    edge_attr = torch.LongTensor(
        np.vectorize(edge_attr_to_idx_dict.get)(edge_attr.values)
    )

    # Get train/val/test masks
    mask = edges["mask"].values
    train_mask = torch.BoolTensor(mask == "train")
    val_mask = torch.BoolTensor(mask == "val")
    test_mask = torch.BoolTensor(mask == "test")

    # Create data object
    data = Data(
        edge_index=edge_index,
        edge_attr=edge_attr,
        train_mask=train_mask,
        val_mask=val_mask,
        test_mask=test_mask,
    )
    return data, edge_attr_to_idx_dict, nodes
