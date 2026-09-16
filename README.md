# Cloud-Based Machine Learning Model Deployment

A responsive web application and REST API for real-time Machine Learning model inference, built with **Python**, **Flask**, and **Scikit-Learn**, and hosted using **Google Cloud Platform (GCP)** infrastructure.

---

## 📌 Project Overview
This project demonstrates an end-to-end Machine Learning pipeline deployed on Google Cloud Platform. Users can input numerical measurements for flower attributes (sepal/petal length and width) via an interactive web interface to receive real-time classification results powered by a trained Random Forest model.

## 🛠️ Tech Stack & Prerequisites
* **Language:** Python 3.10
* **ML Framework:** Scikit-Learn
* **Backend Framework:** Flask, Gunicorn
* **Frontend:** HTML5, CSS3 (Google Material-inspired Design)
* **Cloud Platform:** Google Cloud Platform (GCP Cloud Shell / App Engine / Cloud Run)
* **Version Control:** Git & GitHub

---

## 📁 Repository Structure
```text
cloud-ml-deployment/
│── app.py             # Flask Web Server & API Routing
│── model.py           # Machine Learning Model Training Script
│── model.pkl          # Serialized Trained Model Artifact
│── requirements.txt   # Python Project Dependencies
│── app.yaml           # GCP App Engine Deployment Configuration
│── static/
│   └── style.css      # Custom UI Styling
└── templates/
    └── index.html     # Responsive Web Interface
