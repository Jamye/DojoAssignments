from django.shortcuts import render, HttpResponse
#CONTROLLER
# Create your views here.
# def index(request):
#     response = "Hello, I am your first request"
#     return HttpResponse(response)

def index(request):
    print "blah blah blah blah blah blah blah blah "
    return render(request, "first_app/index.html")
