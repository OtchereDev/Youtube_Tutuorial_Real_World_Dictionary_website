from django.shortcuts import render

def home(request):
    return render(request,'dictionary_app/index.html')
