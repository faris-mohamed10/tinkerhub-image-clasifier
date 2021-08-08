from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from predict import processImg

# Initializing flask application
app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def main():
    return """
        Application is working
    """


@app.route("/predict", methods=["POST"])
def processReq():
    data = request.files["img"]
    data.save("img.jpg")

    resp = processImg("img.jpg")

    print(resp)

    return jsonify(resp)
