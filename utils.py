import os

NEO4J_URL = "bolt://192.168.1.137:7687"
NEO4J_LOGIN = "neo4j"
NEO4J_PASSWORD = "password"
NEO4J_DATABASE = "neo4j"

LOG_FILE = "./log.txt"



def log_to_file(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message)

def clear_log_file():
    with open(LOG_FILE, "w") as f:
        f.write("")


def request(driver, query):
    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(query).data()
        return result
    
def get_driver():
    from neo4j import GraphDatabase
    driver = GraphDatabase.driver(NEO4J_URL, auth=(NEO4J_LOGIN, NEO4J_PASSWORD))
    return driver
