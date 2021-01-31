import requests
import os
from datetime import timedelta

from django.utils import timezone


from .models import WordofDay

def searchWord(word):

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        'x-rapidapi-key': os.getenv('API_KEY') ,
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()


def getRandomWord():

    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random":"true"}

    headers = {
        'x-rapidapi-key': os.getenv('API_KEY'),
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

   

    return response.json()


def word_of_the_day():
    current_word=WordofDay.objects.last()

    if current_word != None:

        deadline=current_word.timestamp+timedelta(24)

        if deadline > timezone.now():
            word = current_word.word
            definition=current_word.definition

            return {
                'word':word,
                'definition':definition
            }

        else:
            current_word.delete()

            random_word=getRandomWord()

            word=random_word['word']
            definition=random_word['results'][0]['definition']

            WordofDay.objects.create(word=word,definition=definition)

            return {
                'word':word,
                'definition':definition
            }

    else:
        random_word=getRandomWord()

        word=random_word['word']
      
        definition=random_word['results'][0]['definition']

        WordofDay.objects.create(word=word,definition=definition)

        return {
            'word':word,
            'definition':definition
        }
