from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request,'rango/index.html',context_dict)
def about(request):
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")
    context_dict = {'boldmessage': 'This tutorial has been put together by Junbai Chen.'}
    return render(request,'rango/about.html',context_dict)