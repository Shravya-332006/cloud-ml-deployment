touch app.py model.py app.yaml requirements.txt
mkdir templates && touch templates/index.html
python3 model.py
gcloud app create --region=us-central
python3 model.py
python3 app.py
mkdir -p static
touch static/style.css
python3 app.py
git init
