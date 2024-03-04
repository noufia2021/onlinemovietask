from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('credentials:login')
    return render(request,'login.html')

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email id already exists")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.info(request,"User created")
                return redirect('credentials:login')
        else:
            messages.info(request,"passwords are not matching")
            return redirect('credentials:register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
