# %%
import os
from functools import wraps
from bottle import Bottle, request, response
import pandas as pd

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


def handle_request(func):
    @wraps(func)
    def wrapper(patient_id, *args, **kwargs):
        if request.method == "OPTIONS":
            response.status = 204
            return

        if not patient_id:
            response.status = 400
            return {"error": "Patient ID is required"}

        try:
            return func(int(patient_id), *args, **kwargs)
        except Exception as e:
            response.status = 500
            return {"error": str(e)}

    return wrapper


def create_patient_result_endpoint(route, response_key, filename):
    @cfr_api_server.route(f"/{route}/<patient_id>", method=["OPTIONS", "GET", "POST"])
    @handle_request
    def endpoint(patient_id):
        data = _read_patient_data_from_file(patient_id, filename)
        return {"patient_id": patient_id, response_key: data}

    return endpoint


def _read_patient_data_from_file(patient_id=None, file=None):
    file_path = os.path.join(RESULTS_DIR, file)
    df = pd.read_csv(file_path)
    patient_data = df[df["patient_id"] == patient_id].to_dict(orient="records")
    return patient_data


get_patients_like_me = create_patient_result_endpoint(
    "patients_like_me", "similar_patients", "checkpoints.patients_like_me_scores.csv"
)
get_causal_gene = create_patient_result_endpoint(
    "causal_gene_discovery",
    "causal_gene",
    "checkpoints.causal_gene_discovery_scores.csv",
)
get_disease_characterization = create_patient_result_endpoint(
    "disease_characterization",
    "disease_characterization",
    "checkpoints.disease_characterization_scores.csv",
)


# print(_get_patients_like_me(15013028))
