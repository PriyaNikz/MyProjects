from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Applicant


def index(request):
    return render(request,"index.html")

def application(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['account']
        material = request.POST['material']
        if Applicant.objects.filter(name=name, email=email).exists():
            messages.info(request, "User or mail already exists!!")
            return redirect('login')
        else:
            application = Applicant.objects.get_or_create(name=name, dob=dob, age=age, gender=gender, phone=phone,email=email, address=address, district=district,
                                                          branch=branch,account=account, material=material)
            application.save()
            messages.info(request, "Application accepted!!")
            return redirect('login')
    else:
        messages.info(request, "Please try again later!")
        return redirect('/')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!!")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "New user created!!")  # Moved the print message to a message
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('/')  # Make sure to return here as well
    return render(request, "register.html")
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, "application.html")
        else:
            messages.info(request,"Invalid username or password!!")
            return redirect('/')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')