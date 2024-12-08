#%%
from pronto import Ontology

mondo = Ontology("./mondo-rare.obo")

doid_to_mondo = {}

for term in mondo.terms():
    for xref in term.xrefs:
        if xref.id.startswith("DOID:"):
            doid_to_mondo[xref.id] = term.id

example_doid = "DOID:9352"  
if example_doid in doid_to_mondo:
    print(f"MONDO ID for {example_doid} is {doid_to_mondo[example_doid]}")
else:
    print(f"No mapping found for {example_doid}")
