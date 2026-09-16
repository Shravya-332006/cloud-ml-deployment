import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model, target_names = pickle.load(f)

# Image mappings for predicted species
FLOWER_IMAGES = {
    "setosa": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Iris_setosa_december_2009_1.jpg",
    "versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
}

@app.route("/")
def home():
    defaults = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    return render_template("index.html", inputs=defaults)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        inputs = {
            "sepal_length": float(request.form["sepal_length"]),
            "sepal_width": float(request.form["sepal_width"]),
            "petal_length": float(request.form["petal_length"]),
            "petal_width": float(request.form["petal_width"])
        }

        features = [[inputs["sepal_length"], inputs["sepal_width"], inputs["petal_length"], inputs["petal_width"]]]
        prediction = model.predict(features)[0]
        species = target_names[prediction]
        image_url = FLOWER_IMAGES.get(species, "")

        return render_template("index.html", prediction_text=f"Predicted Species: {species}", species=species, image_url=image_url, inputs=inputs)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)