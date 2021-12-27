# Main module.

# $env:FLASK_APP = "similar-texts-recognition"
# flask run
# http://127.0.0.1:5000//similar-recognition


from flask import Flask
from flask import request
from flask import render_template

from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import cosine
from numpy.linalg import norm


# Function for calculation similarity between two strings.
# Input: two strings "text_1" and "text_2".
# Output: similarity metric.
def similarity(text_1=None, text_2=None):
    # If one of the values is absent, zero metric value will be returned.
    if (text_1 is None) or (text_2 is None):
        return 0

    # A list of stop words that shouldn't be considered during vectorization - prepositions.
    list_stop_words = ['about', 'above', 'across', 'after', 'against', 'among', 'around', 'at', 'before', 'behind',
                       'below', 'beside', 'between', 'by', 'down', 'during', 'for', 'from', 'in', 'inside', 'into',
                       'near', 'of', 'off', 'on', 'out', 'over', 'through', 'to', 'toward', 'under', 'up', 'with',
                       'aboard', 'along', 'amid', 'as', 'beneath', 'beyond', 'but', 'concerning', 'considering',
                       'despite', 'except', 'following', 'like', 'minus', 'next', 'onto', 'opposite', 'outside',
                       'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than', 'till', 'underneath',
                       'unlike', 'until', 'upon', 'versus', 'via', 'within', 'without']

    # Amount of words in the first string.
    text_1_len = len(text_1[0].split(' '))

    # If text without 'stop_words' not so long, less than thirty words, unigrams and bigrams will be considered.
    # Otherwise only unigrams will be considered.
    if text_1_len >= 30:
        dict_settings_text_small = {'stop_words': list_stop_words,
                                    'ngram_range': (1, 1)}
    else:
        dict_settings_text_small = {'stop_words': list_stop_words,
                                    'ngram_range': (1, 2)}

    cv = CountVectorizer(**dict_settings_text_small)

    vector_1 = cv.fit_transform([text_1])
    vector_1 = vector_1.toarray()

    vector_2 = cv.transform([text_2])
    vector_2 = vector_2.toarray()

    # If vector_2 consists of only zero values, cosine distance will be calculated incorrect.
    # Also it means there are no similar words in second string, so the metric will be zero.
    if norm(vector_2) == 0:
        return 0

    metric_similarity = 1 - cosine(vector_1, vector_2)

    return metric_similarity


app = Flask(__name__)


@app.route("/similar-recognition", methods=['POST', 'GET'])
def similar_recognition():
    text_1 = request.args.get('text_1')
    text_2 = request.args.get('text_2')

    metric_similarity = similarity(text_1, text_2)

    # text_1 = text_1 if text_1 is not None else f'No text has been received'
    # text_2 = text_2 if text_2 is not None else f'No text has been received'

    if request.method == 'GET':
        return render_template('similar-texts-recognition_get.html', text_1=text_1, text_2=text_2,
                               metric_similarity=metric_similarity)
    elif request.method == 'POST':
        return render_template('similar-texts-recognition_post.html', text_1=text_1, text_2=text_2,
                               metric_similarity=metric_similarity)
