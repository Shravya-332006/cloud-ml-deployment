import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model, target_names = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [[
        float(request.form["sepal_length"]),
        float(request.form["sepal_width"]),
        float(request.form["petal_length"]),
        float(request.form["petal_width"])
    ]]
    result = target_names[model.predict(features)[0]]
    return render_template("index.html", prediction_text=f"Predicted Species: {result}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)