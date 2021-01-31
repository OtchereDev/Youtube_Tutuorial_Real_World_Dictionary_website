import requests
import os

def searchWord(word):

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        'x-rapidapi-key': os.getenv('API_KEY') ,
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()

