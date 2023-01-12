from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# A view is returns a response to a request
# Hence it's more of a request handler

def say_hello(request):
    #We can return a simple text response
    #return HttpResponse("Hello World!") 
    x = 1 
    y = 2
    #Or we can return a html file
    return render(request, "hello.html", {"name":"Ethan"})
