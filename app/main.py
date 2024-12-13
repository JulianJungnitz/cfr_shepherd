from bottle import Bottle, static_file

from FeatureCloud.app.api.http_ctrl import api_server
from FeatureCloud.app.engine.app import app

import states

from app.cfr_api import  cfr_api_server


server = Bottle()

if __name__ == '__main__':
    app.register()
    print("Starting server")
    server.mount('/api', api_server)
    server.mount('/cfr_api', cfr_api_server)
    server.run(host='0.0.0.0', port=5000)
    print("Server started")
