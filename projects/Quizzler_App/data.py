import requests
response = requests.get(url="https://opentdb.com/api.php?amount=1&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()

question_data = data["results"]