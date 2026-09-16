import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model, target_names = pickle.load(f)

@app.route("/")
def home():
    # Default initial values
    defaults = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    return render_template("index.html", inputs=defaults)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract user inputs from form
        inputs = {
            "sepal_length": float(request.form["sepal_length"]),
            "sepal_width": float(request.form["sepal_width"]),
            "petal_length": float(request.form["petal_length"]),
            "petal_width": float(request.form["petal_width"])
        }

        # Make prediction with modified parameters
        features = [[inputs["sepal_length"], inputs["sepal_width"], inputs["petal_length"], inputs["petal_width"]]]
        prediction = model.predict(features)[0]
        result = target_names[prediction]

        # Pass both the prediction result AND the submitted user inputs back to index.html
        return render_template("index.html", prediction_text=f"Predicted Species: {result}", inputs=inputs)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)