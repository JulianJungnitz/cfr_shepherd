from bottle import Bottle

from FeatureCloud.app.api.http_ctrl import api_server
from FeatureCloud.app.api.http_web import web_server

from FeatureCloud.app.engine.app import app

import states

from time import sleep

server = Bottle()



if __name__ == '__main__':
    print("Starting server", )
    app.register()
    server.mount('/api', api_server)
    server.mount('/web', web_server)
    server.run(host='localhost', port=5000)
    print("Server started", )