from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return HttpResponse("Hello, world. You're at the home index.")

@login_required(login_url='/login/')
def homepagediff(request):
    peoples = Person.objects.all() 
    # peoples=[
    #     {'name':'laku','age':19,'email':'lakshaygoyallg.vercel.app'},
    #     {'name':'lucy','age':19,'email':'fangwolflg.vercel.app'},
    #     {'name':'chinna','age':200,'email':'nalli'}
    # ]
    

    if request.GET.get('search'):
        peoples = peoples.filter(name__icontains = request.GET.get('search'))


    return render(request,'home.html',context={'peoples':peoples})

@login_required(login_url='/login/')
def formpage(request):
    
    if request.method == "POST":
        data = request.POST
        
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        user = request.user
        print(name)
        
        Person.objects.create(name=name, age=age, email=email,user=user)
        return redirect("/home")
    
    peoples = Person.objects.all() 
    return render(request, 'form.html',context={'peoples':peoples})

@login_required(login_url='/login/')
def delpeople(request,id):
    queryset=Person.objects.get(id=id)
    queryset.delete()
    return redirect('/home')

@login_required(login_url='/login/')
def updpeople(request,id):
    queryset=Person.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
    
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
    
        queryset.name=name
        queryset.age=age
        queryset.email=email
    
        queryset.save()
        return redirect("/home")
    
    return render(request,'updform.html',context={'person':queryset})

def signuppage(request):
    
    if request.method != "POST":
        return render(request,'signup.html')
    data = request.POST

    first_name = data.get('name')
    username = data.get('username')
    password = data.get('password')

    user = User.objects.filter(username=username)
    if user.exists():
        messages.error(request, 'Username already exists!!!')
        return redirect('/login')

    user = User.objects.create_user(first_name=first_name,username=username)
    user.set_password(password)

    user.save()
    print(user)
    messages.info(request, 'Account created')
    return redirect("/login")

def loginpage(request):
    
    if request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('/login')

        else:
            login(request,user)
            return redirect('/home')

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/login')


