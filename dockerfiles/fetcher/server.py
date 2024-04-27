from flask import Flask, request, jsonify
from os.path import join, dirname

import github as gutl

app = Flask(__name__)

# Constants
cache_path = "/cache"

@app.route('/fetch', methods=['POST'])
def fetch_files():
    # Get JSON data from request
    data = request.get_json()
    fetch_list = data.get('fetch_list')

    # Process each entry in the fetch list
    if fetch_list:
        for entry in fetch_list:
            if entry["type"] == "github":
                print("Fetching files for repository:", entry['repository'])
                gutl.get_repo(entry, cache_path)
        return jsonify({"message": "Fetch process initiated"}), 200
    else:
        return jsonify({"error": "Invalid or missing 'fetch_list' in request"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)