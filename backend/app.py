from flask import Flask, jsonify, send_from_directory
import os
import requests
from flask_cors import CORS

static_path = os.getenv('STATIC_PATH','static')
template_path = os.getenv('TEMPLATE_PATH','templates')

app = Flask(__name__, static_folder=static_path, template_folder=template_path)
CORS(app)

@app.route('/ucdavis-news')
def get_news():
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22UC%20Davis%22&api-key=w4rcy5YA6GG99HeECAyyBwmfzARZefFx"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path=''):
    if path != '' and os.path.exists(os.path.join(static_path,path)):
        return send_from_directory(static_path, path)
    return send_from_directory(template_path, 'index.html')

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)),debug=debug_mode)