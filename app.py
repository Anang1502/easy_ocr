import os
import time
import config as cf
import easyocr
import cv2 as cv
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
from pdf2image import convert_from_path
model_time = time.time()
reader = easyocr.Reader(['en'])
print("model time {}".format(str(time.time() - model_time)))
# from src.utils import extract_text_easyocr

app = Flask(__name__, instance_path="/{cf.BASE_PATH}/instance")
Swagger(app)


def convert2image(file_path, file_name):
    output_folder = os.path.join(cf.BASE_PATH, "data", "converted_img")
    convert_from_path(file_path, dpi=350, output_folder=output_folder, fmt='jpeg',
                      thread_count=2, userpw=None)
    return output_folder


def extract_text(file_path):
    try:
        text_time = time.time()
        result = reader.readtext(file_path)
        print("text extraction time {}".format(str(time.time() - text_time)))
        return result
    except Exception as error:
        print(error)


@app.route('/api/v1/process_file', methods=["POST", "OPTIONS"])
@swag_from(os.path.join(cf.BASE_PATH, "api_doc", "process_file.yml"))
def main():
    try:
        start_time = time.time()
        file = request.files['file']
        file_name = file.filename
        file_path = os.path.join(cf.BASE_PATH, "data", "files", file_name)
        file.save(file_path)
        print("file is saved")
        image_dir = convert2image(file_path, str(file.filename))
        print(len(os.listdir(image_dir)))
        c = 0
        for image in os.listdir(image_dir):
            result = extract_text(os.path.join(image_dir, image))
            # image1 = cv.imread(os.path.join(image_dir, image))
        #     for (bbox, text, prob) in result:
        #         # text_.append(text)
        #         (tl, tr, br, bl) = bbox
        #         tl = (int(tl[0]), int(tl[1]))
        #         tr = (int(tr[0]), int(tr[1]))
        #         # br = (int(br[0]), int(br[1]))
        #         br = (int(br[0]), int(br[1]))
        #         bl = (int(bl[0]), int(bl[1]))
        #         cv.rectangle(image1, tl, br, (0, 255, 0), 2)
        #         cv.putText(image1, text, (tl[0], tl[1] - 10),
        #                     cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        #     plt.imsave((os.path.join(cf.BASE_PATH, "data", "box_img", 'image{0}.png'.format(str(c)))), image1)
        print("total processing time : {}".format(str(time.time() - start_time)))
        print(result)
        return jsonify({'result': "Process Completed"})
    except Exception as error:
        print(error)


if __name__ == '__main__':
    app.run(host='localhost', port=5006)