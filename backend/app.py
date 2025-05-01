from flask import Flask, jsonify, send_from_directory
import os
import requests
from flask_cors import CORS

<<<<<<< HEAD
# Configure folder names via environment (with defaults)
static_path = os.getenv('STATIC_PATH','static') # Directory for compiled frontend assets
template_path = os.getenv('TEMPLATE_PATH','templates') # Directory for HTML templates

# Initialize Flask app, telling it where to find static files and templates
app = Flask(__name__, static_folder=static_path, template_folder=template_path)
CORS(app)

@app.route('/api/ucdavis-news') # API endpoint to fetch UC Davis–related articles
def get_news():
    # Build the request URL with query parameters and API key
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22UC%20Davis%22&api-key=w4rcy5YA6GG99HeECAyyBwmfzARZefFx"
    response = requests.get(url) # Perform HTTP GET
    data = response.json() # Parse response as JSON
    return jsonify(data) # Return JSON to client

@app.route('/') # Serve index for root
@app.route('/<path:path>') # Serve other frontend routes
def serve_frontend(path=''):
     # If the path matches a file in static folder, serve that file directly
    if path != '' and os.path.exists(os.path.join(static_path,path)):
        return send_from_directory(static_path, path)
    # Otherwise, serve the main HTML template
    return send_from_directory(template_path, 'index.html')

if __name__ == '__main__':
    # Determine debug mode from FLASK_ENV
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    # Start Flask development server on specified host and port
    app.run(host='0.0.0.0', 
            port=int(os.environ.get('PORT', 8000)),
            debug=debug_mode
            )
=======
static_path = os.getenv('STATIC_PATH','static')
template_path = os.getenv('TEMPLATE_PATH','templates')

app = Flask(__name__, static_folder=static_path, template_folder=template_path)
CORS(app)

@app.route('/api/ucdavis-news')
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
>>>>>>> dc67a61cf32ecee289265346fa7282031c1914ea
