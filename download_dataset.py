import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset and the download path
dataset_name = 'alkanerturan/vehicledetection'  # Replace with actual dataset path on Kaggle
download_path = 'dataset/'  # Define where you want to store the dataset

# Ensure the download directory exists
os.makedirs(download_path, exist_ok=True)

# Download dataset
print(f"Downloading {dataset_name}...")
api.dataset_download_files(dataset_name, path=download_path, unzip=False)

# Find the downloaded zip file
zip_file = os.path.join(download_path, dataset_name.split('/')[-1] + '.zip')

# Unzip the dataset
print(f"Unzipping {zip_file}...")
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(download_path)

# Optionally, remove the zip file after extraction
os.remove(zip_file)

print(f"Dataset downloaded and extracted to {download_path}")
