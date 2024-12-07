# %%
import os
from functools import wraps
from bottle import Bottle, request, response
import pandas as pd
from typing import Callable, Any
import utils as utils

current_dir = os.path.dirname(os.path.realpath(__file__))
RESULTS_DIR = os.path.join(current_dir, "SHEPHERD/data/results")

cfr_api_server = Bottle()


@cfr_api_server.hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    requested_headers = request.headers.get("Access-Control-Request-Headers")
    if requested_headers:
        response.headers["Access-Control-Allow-Headers"] = requested_headers
    else:
        response.headers["Access-Control-Allow-Headers"] = (
            "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token"
        )


@cfr_api_server.route("/", method=["OPTIONS", "GET", "POST"])
def api_root():
    if request.method == "OPTIONS":
        response.status = 204
        return
    return (
        "CFR API Server\n"
    )


def handle_request(func: Callable) -> Callable:
    """Base decorator for handling API requests"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> dict:
        if request.method == "OPTIONS":
            response.status = 204
            return
            
        try:
            result = func(*args, **kwargs)
            return {"data": result}
        except Exception as e:
            response.status = 500
            return {"message": str(e)}
            
    return wrapper

def handle_patient_request(func: Callable) -> Callable:
    """Decorator for handling patient-specific API requests"""
    @handle_request
    @wraps(func)
    def wrapper(patient_id: str, *args, **kwargs) -> Any:
        # Validate patient_id
        if not patient_id:
            response.status = 400
            return {"message": "Patient ID is required"}
            
        return func(int(patient_id), *args, **kwargs)
            
    return wrapper

    return wrapper

def create_patient_result_endpoint(route, response_key, filename):
    @cfr_api_server.route(f"/{route}/<patient_id>", method=["OPTIONS", "GET", "POST"])
    @handle_patient_request
    def endpoint(patient_id):
        data = _read_patient_data_from_file(patient_id, filename)
        return {"patient_id": patient_id, response_key: data}

    return endpoint

@cfr_api_server.route(f"/query", method=["OPTIONS", "POST"])
@handle_request
def endpoint():
    data = request.json
    query = data.get("query")
    if not query:
        response.status = 400
        return {"message": "Query is required"}
    driver = utils.connect_to_neo4j()
    result = utils.execute_query(driver, query)
    return result

def create_has_result_endpoint(route, filename):
    @cfr_api_server.route(f"/{route}", method=["OPTIONS", "GET", "POST"])
    @handle_request
    def endpoint():
        # check if file exists
        file_path = os.path.join(RESULTS_DIR, filename)
        if not os.path.exists(file_path):
            response.status = 404
            return {"message": "Result file not found"}
        df = pd.read_csv(file_path)
        if df.empty:
            response.status = 404
            return {"message": "No results found"}
        return True


    return endpoint


def _read_patient_data_from_file(patient_id=None, file=None):
    file_path = os.path.join(RESULTS_DIR, file)
    df = pd.read_csv(file_path)
    patient_data = df[df["patient_id"] == patient_id].to_dict(orient="records")
    return patient_data


patient_like_me_result_file= "checkpoints.patients_like_me_scores.csv"
causal_gene_result_file = "checkpoints.causal_gene_discovery_scores.csv"
disease_characterization_result_file = "checkpoints.disease_characterization_scores.csv"

get_patients_like_me = create_patient_result_endpoint(
    "patients_like_me", "similar_patients", patient_like_me_result_file
)
get_causal_gene = create_patient_result_endpoint(
    "causal_gene_discovery",
    "causal_gene",
    causal_gene_result_file,
)
get_disease_characterization = create_patient_result_endpoint(
    "disease_characterization",
    "disease_characterization",
   disease_characterization_result_file,
)

has_patients_like_me_result = create_has_result_endpoint("has_patients_like_me", patient_like_me_result_file)
has_causal_gene_result = create_has_result_endpoint("has_causal_gene_discovery", causal_gene_result_file)
has_disease_characterization_result = create_has_result_endpoint("has_disease_characterization", disease_characterization_result_file)


# print(_get_patients_like_me(15013028))
