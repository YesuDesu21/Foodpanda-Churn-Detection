#Run this if you do not have the file yet
import kaggle
import os 
from pathlib import Path

kaggle.api.authenticate()

dataset_path = 'data/unprocessed'

# Check if dataset folder exists AND contains files
if not os.path.exists(dataset_path) or not os.listdir(dataset_path):
    print("Dataset folder is empty or doesn't exist. Downloading...")
    kaggle.api.dataset_download_files(
        "nabihazahid/foodpanda-analysis-dataset-2025", 
        path=dataset_path, 
        unzip=True,
        quiet=False
    )
