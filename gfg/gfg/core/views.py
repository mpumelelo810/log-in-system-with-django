from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
      return render(request,"core/home.html")

def signup(request):
    if request.method=="POST":
         username=request.POST['username']
         Firstname=request.POST['Firstname']
         Lastname=request.POST['Lastname']
         email=request.POST['email']
         password=request.POST['password']
         confirmpassword=request.POST['confirmpassword']
         myuser=User.objects.create_user(username, email, password)
         myuser.Firstname=Firstname
         myuser.Lastname= Lastname
         myuser.save() 
         messages.success(request, "your account has been successfully created")
         return redirect('signin')
    return render(request,"core/signup.html")
def signin(request):
    if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         user=authenticate(username=username, password=password)
         if user is not None:
              login(request,user)
              Firstname=user.Firstname
              Fname = request.POST['Firstname']
              return render(request,"core/home.html",{Fname})
         else:
              messages.error(request,"Bad credentials")
              return redirect('home')
    return render(request,"core/signin.html")
def signout(request):
    pass

