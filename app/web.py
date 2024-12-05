import os
from bottle import Bottle, run, request, response, static_file

FLUTTER_BUILD_DIR = 'frontend/build/web'

web_server= Bottle()

@web_server.route('/')
def index():
    return static_file('index.html', root=FLUTTER_BUILD_DIR)


@web_server.route('/<filepath:path>')
def serve_static(filepath):
    file_path = os.path.join(FLUTTER_BUILD_DIR, filepath)
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return static_file(filepath, root=FLUTTER_BUILD_DIR)
    else:
        return static_file('index.html', root=FLUTTER_BUILD_DIR)