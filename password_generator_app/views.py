from django.shortcuts import render
from django.http import HttpResponse
import random 

# Create your views here.

#def home(request):
    #return HttpResponse('<h1> Hello! Welcome to the website! </h1>')

def home(request):
    return render(request, 'password_generator_app/home.html', {'password': ''} )

def about(request):
    return render(request, 'password_generator_app/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('UpperCase'):
         characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*)('))

    if request.GET.get('Numbers'):
        characters.extend(list('0,1,2,3,4,5,6,7,8,9'))

    length = int(request.GET.get('Length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'password_generator_app/password.html', {'password': thepassword})
