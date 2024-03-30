import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name="HateSpeechClassification"

list_of_files = [
    f"{package_name}/components/__init__.py",
    f"{package_name}/components/data_ingestion.py",
    f"{package_name}/components/data_transforamation.py",
    f"{package_name}/components/model_trainer.py",
    f"{package_name}/components/model_evaluation.py",
    f"{package_name}/components/model_pusher.py",
    f"{package_name}/configuration/__init__.py",
    f"{package_name}/configuration/gcloud_syncer.py",
    f"{package_name}/constants/__init__.py",
    f"{package_name}/entity/__init__.py",
    f"{package_name}/entity/config_entity.py",
    f"{package_name}/entity/artifact_entity.py",
    f"{package_name}/exception/__init__.py",
    f"{package_name}/logger/__init__.py",
    f"{package_name}/pipeline/__init__.py",
    f"{package_name}/pipeline/train_pipeline.py",
    f"{package_name}/pipeline/prediction_pipeline.py",
    f"{package_name}/ml/__init__.py",
    f"{package_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

# here will use the file handling

