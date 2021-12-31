# Main module.

# $env:FLASK_APP = "emotion-detection"
# flask run
# http://127.0.0.1:5000//emotion-detection

# https://huggingface.co/nateraw/bert-base-uncased-emotion
# https://metatext.io/models/nateraw-bert-base-uncased-emotion


from flask import Flask
from flask import request
from flask import render_template

from transformers import AutoTokenizer, AutoModelForSequenceClassification


# Function for detection emotions.
# Input: string "text".
# Output: string, name of recognized emotion.
def detect_emotion(text):
    # Loading pretrained tokenizer and model.
    tokenizer = AutoTokenizer.from_pretrained("nateraw/bert-base-uncased-emotion")
    model = AutoModelForSequenceClassification.from_pretrained("nateraw/bert-base-uncased-emotion")

    # Transform input tokens.
    inputs = tokenizer(text, return_tensors="pt")

    # Model apply.
    outputs = model(**inputs)

    # Dictionary with emotions and tensors' values.
    dict_emotion = {'sadness':  float(outputs[0][0][0].detach().numpy()),
                    'joy':      float(outputs[0][0][1].detach().numpy()),
                    'love':     float(outputs[0][0][2].detach().numpy()),
                    'anger':    float(outputs[0][0][3].detach().numpy()),
                    'fear':     float(outputs[0][0][4].detach().numpy()),
                    'surprise': float(outputs[0][0][5].detach().numpy())}

    # Return the most probable emotion.
    return max(dict_emotion, key=dict_emotion.get)


app = Flask(__name__)


@app.route("/emotion-detection", methods=['POST'])
def emotion_detection():
    text = request.args.get('text')

    emotion = detect_emotion(text)

    return render_template('emotion-detection_post.html', text=text, emotion=emotion)
