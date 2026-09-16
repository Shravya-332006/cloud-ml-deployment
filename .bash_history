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
git add .
git commit -m "Initial commit - GCP ML Deployment Project"
git config --global user.email "Shravya-332006"
git config --global user.email "sshravyaharikant@gmail.com"
git config --global user.name "Shravya-332006"
git commit -m "Initial commit - GCP ML Deployment Project"
git branch -M main
git remote add origin https://github.com/Shravya-332006/cloud-ml-deployment.git
git push -u origin main
git remote set-url origin https://Shravya-332006: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@github.com/Shravya-332006/cloud-ml-deployment.git
git push -u origin main
git add .
git commit -m "Enhanced UI styling and added dynamic flower image output"
git push
git push -f origin main
python app.py
