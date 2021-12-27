# Main module.

# $env:FLASK_APP = "image-text-recognition"
# flask run
# http://127.0.0.1:5000//text-recognition


from flask import Flask
from flask import request
from flask import render_template

import easyocr


# Function for OCR.
# Input: image.
# Output: recognized text.
def ocr(image):
    reader = easyocr.Reader(lang_list=['en'], gpu=False)
    return reader.readtext(image, detail=0)


app = Flask(__name__)


@app.route("/text-recognition", methods=['POST'])
def text_recognition():
    image = request.files.get('image')
    text = ocr(image.read())
    text = ' '.join(text)
    return render_template('image-text-recognition_post.html', text=text)
