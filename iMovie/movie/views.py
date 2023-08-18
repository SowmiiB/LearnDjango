from django.shortcuts import render
from django.http import HttpResponse
from movie import models
# Create your views here.

def homepage(request):
    film = models.Movie()
    film.title = 'Catch Me If You Can'
    film.language ='English'
    film.poster = 'catch_me_if_you_can.jpg'
    film.rating = 4.8
    film.ticket_cost = '$5'

    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        if uname.lower() == 'admin' and pwd == '1234':
            return render(request,'index.html',{'film1':film})
        else:
            return HttpResponse('<h2> Invalid User! </h2>')

