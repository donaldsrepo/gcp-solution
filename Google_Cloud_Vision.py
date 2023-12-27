"""
need to install google-cloud-vision (GCP SDK) from conda -c conda-forge
conda install -c conda-forge pillow=10.1.0 pandas=2.1.2 google-cloud-vision=3.4.5 scikit-learn=1.3.2 ipykernel jupyterlab notebook python=3.12.0
to set up in jupyterlabs:
python -m ipykernel install --user --name=gcp-cloud-vision
repo: https://github.com/donaldsrepo/gcp-solution
"""

import os
from os import listdir
from os.path import isfile, join
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='vision_key.json'
from google.cloud import vision
from my_timer import my_timer
import time

def detect_text(path):
    client = vision.ImageAnnotatorClient()
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    ocr_text = []
    for text in texts:
        ocr_text.append(f"\r\n{text.description}")
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return texts[0].description

@my_timer
def main():
    mypath = "../content/"
    only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for image_path in only_files:
        text = detect_text(mypath+image_path)
        print(image_path)
        print(text)

if __name__ == "__main__":
     main()
