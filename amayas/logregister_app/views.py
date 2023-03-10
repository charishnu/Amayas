from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from home_app.views import home

# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name = request.POST['first_name']

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,password=password1,email=email)
                user.save();
                print('user created')
        else:
            print("password not mathch")
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'registration.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



