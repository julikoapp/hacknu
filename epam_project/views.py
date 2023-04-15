from django.http import HttpResponse

def index(request):
    return HttpResponse(" Helllo, word")

def login(request):
    return  HttpResponse("Login")

def register(request):
    return HttpResponse("Register")