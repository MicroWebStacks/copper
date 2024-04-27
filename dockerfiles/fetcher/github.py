import os
import requests
import zipfile
from pathlib import Path
from os.path import join
from os import makedirs

def get_repo(params, cache_path):
    repository  = params["repository"]
    ref         = params["ref"]
    path        = join(cache_path,params["path"])
    file_filter = params["filter"]
    # GitHub URL to download the repository as a zip file
    url = f"https://api.github.com/repos/{repository}/zipball/{ref}"

    # Download the zip file
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for request errors

    # Define the path for saving the downloaded zip file temporarily
    zip_file = join(path, 'repo.zip')
    makedirs(path, exist_ok=True)
    # Write the zip file to the disk
    with open(zip_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # Extract specific files from the zip
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # List all file names in the zip
        all_files = zip_ref.namelist()
        # Filter files based on the given glob pattern
        filtered_files = [f for f in all_files if Path(f).match(file_filter)]
        # Extract only the filtered files
        for file in filtered_files:
            zip_ref.extract(file, path)

    # Remove the downloaded zip file after extraction
    os.remove(zip_file)
