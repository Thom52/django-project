from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse("Hello World!")
    if requests.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)

