import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'English Question Attempt':7, 'English Total Marks':7, 'English Scores':5, 'English PCT':51})

print(r.json())