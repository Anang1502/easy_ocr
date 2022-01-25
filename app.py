import os
import config as cf
import easyocr
from flask import Flask, request
from flasgger import Swagger, swag_from
from src.utils import extract_text_easyocr

app = Flask(__name__, instance_path="/{cf.BASE_PATH}/instance")
Swagger(app)


def extract_text(file_path):
    try:
        reader = easyocr.Reader(['en'])
        result = reader.readtext(file_path)
        return result
    except Exception as error:
        print(error)


@app.route('/api/v1/process_file', methods=["POST", "OPTIONS"])
@swag_from(os.path.join(cf.BASE_PATH, "api_doc", "process_file.yml"))
def main():
    try:
        file = request.files['file']
        file_name = file.filename
        file_path = os.path.join(cf.BASE_PATH, "files", file_name)
        file.save(os.path.join(cf.BASE_PATH, "files", file_name))
        print("file is saved")
        result = extract_text(file_path)
        print(result)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    app.run(host='localhost', port=5006)
