from django.shortcuts import render

def index(response):
    return render(response, 'index.html')
def contact(response):
    return render(response, 'contact.html')
