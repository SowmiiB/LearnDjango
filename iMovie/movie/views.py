from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        if uname.lower() == 'admin' and pwd == '1234':
            return render(request,'index.html',{'username':uname})
        else:
            return HttpResponse('<h2> Invalid User! </h2>')

