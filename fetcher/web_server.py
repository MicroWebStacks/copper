from flask import Flask, request, jsonify

from utils import github as gutl

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
        results = []
        for entry in fetch_list:
            if entry["type"] == "github":
                print("Fetching files for repository:", entry['repository'])
                result = gutl.get_repo(entry, cache_path)
                entry.update(result)
                results.append(entry)
        return jsonify(results), 200
    else:
        return jsonify({"error": "Invalid or missing 'fetch_list' in request"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
