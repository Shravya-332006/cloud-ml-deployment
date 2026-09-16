import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

data = load_iris()
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(data.data, data.target)

with open("model.pkl", "wb") as f:
    pickle.dump((clf, data.target_names.tolist()), f)
print("Model saved to model.pkl")