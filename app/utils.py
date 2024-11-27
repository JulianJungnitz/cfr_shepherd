import logging
import yaml
import colorama
from neo4j import GraphDatabase
import os
import subprocess

APP_DIR  = os.path.dirname(os.path.realpath(__file__))
SHEPHERD_DIR = APP_DIR + "/SHEPHERD"
print("APP_DIR: ", APP_DIR)
print("SHEPHERD_DIR: ", SHEPHERD_DIR)


def is_running_in_docker():
    if os.path.exists('/.dockerenv'):
        return True
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            for line in f:
                if 'docker' in line:
                    return True
    except Exception:
        pass
    return False

if is_running_in_docker():
    INPUT_DIR = '/mnt/input'
    OUTPUT_DIR = '/mnt/output'
    print("Running inside Docker container.")
else:
    INPUT_DIR = './..'
    OUTPUT_DIR = './..'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print("Current directory: ", current_dir)
    print("Running on local machine.")







def read_config(file_path=f"{INPUT_DIR}/config.yml",):
    try:
        with open(file_path, "r") as config_file:
            config = yaml.safe_load(config_file)
        return config
                
    except FileNotFoundError:
        print(f"Config file '{file_path}' not found.")



def get_neo4j_credentials():
    config = read_config()
    neo4j_credentials = config.get("neo4j_credentials", {})
    NEO4J_URI = neo4j_credentials.get("NEO4J_URI", "")
    NEO4J_USERNAME = neo4j_credentials.get("NEO4J_USERNAME", "")
    NEO4J_PASSWORD = neo4j_credentials.get("NEO4J_PASSWORD", "")
    NEO4J_DB = neo4j_credentials.get("NEO4J_DB", "")
    print(f"Neo4j Connect to {NEO4J_URI} using {NEO4J_USERNAME}")
    return NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, NEO4J_DB


def connect_to_neo4j():
    print("Connecting to Neo4j")
    config = get_neo4j_credentials()
    global NEO4J_DB
    NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, NEO4J_DB = config
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    print("Connected to Neo4j")
    
    return driver

def execute_query(driver, query):
    with driver.session(database=NEO4J_DB) as session:
        try:
            print(query)
            res = session.run(query).data()
            print(f"Query returned {len(res)} records")
            return res
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            session.close()

def document(y_pred, y_true,):
    # shapes - features - typpes of features (with numbers)
    # accuracy + precision + recall
    # f1 score
    pass



def run_subprocess(command):
    try:
        result = subprocess.run(
            command,
            text=True,
            check=True 
        )
        print('Command executed successfully.')
        print('Output:')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print('An error occurred while executing the command.')
        print('Return code:', e.returncode)
        print('Error output:')
        print(e.stderr)