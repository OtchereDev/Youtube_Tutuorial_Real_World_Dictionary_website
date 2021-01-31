from django.shortcuts import render
import requests
import os

from .helpers import searchWord,word_of_the_day

def home(request):

    word_of_day=word_of_the_day()

    context={
        'method':'GET',
        'word':word_of_day['word'],
        'definition':word_of_day['definition']
    }

    if request.method=='POST':

        user_word=request.POST.get('user_word')


        result=searchWord(user_word)

       
        try:
            context={
                'method':'POST',
                'search_word':result['word'],
                'results':result['results'],
                'pronunciations':result['pronunciation']
            }

        except KeyError:
            context={
                'error':result['message'],
                'failure': True
            }

    return render(request,'dictionary_app/index.html',context=context)
    
