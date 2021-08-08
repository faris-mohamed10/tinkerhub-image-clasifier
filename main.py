from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from predict import processImg

# Initializing flask application
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def home():
    return render_template('form.html', title='Home')


@app.route("/predict", methods=["POST"])
def processReq():
    data = request.files["img"]
    data.save("img.jpg")

    resp = processImg("img.jpg")

    text = "it is a <b>"+resp['label'] + \
        "</b> with confidence <b>"+resp['confidence']+"</b>"

    return text
