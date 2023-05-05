from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email     = request.POST['email']
        username  = request.POST['username']
        password  = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists!!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

            user.save()
            return redirect('login')
            print("New user created!!")
        else:
            messages.info(request, "Password not matching")
        return redirect('/')
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password!!")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')