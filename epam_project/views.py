from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages


def index(request):
    return HttpResponse(" Helllo, word")

def login(request):
    return  HttpResponse("Login")

def register(request):
    error = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if password != repeat_password:
                error = "Пароли не совпадают"
                context = {"form" : form, "error": error}
                #return render(request=request, "register_form.html", context=context)
                return render(request, "register_form.html", context=context)
            # CREATE NEW CLIENT LOGIC?? 
            return redirect("/") 
    else:
        form = RegisterForm()
		
    context = {
        "form" : form, 
        "error": error,
    }
    return render(request, "register_form.html",context=context )

def login(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # OPEN APPROPRIATE MAIN PAGE
            return redirect("/") 
    else:
        form = LoginForm()
		
    context = {
        "form" : form, 
        "error": error,
    }
    return render(request, "login_form.html",context=context )
