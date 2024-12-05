import os
from bottle import Bottle, request, response



cfr_api_server = Bottle()

@cfr_api_server.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    requested_headers = request.headers.get('Access-Control-Request-Headers')
    if requested_headers:
        response.headers['Access-Control-Allow-Headers'] = requested_headers
    else:
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        
@cfr_api_server.route('/', method=['OPTIONS', 'GET'])
def api_root():
    if request.method == 'OPTIONS':
        response.status = 204
        return
    return 'API'