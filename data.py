import requests

# This script fetches trivia questions from an API and stores them in a variable.

paramameters = {
    "amount": "10",
    "type": "boolean",
}

connection = requests.get("https://opentdb.com/api.php", params=paramameters)
connection.raise_for_status()
data = connection.json()

question_data = data["results"]
