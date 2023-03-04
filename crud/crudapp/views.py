from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages

# Create your views here.

def home(request):
    alluser = User.objects.all()

    if request.method == 'POST':
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        password = request.POST.get('password','')
        address = request.POST.get('address','')
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exist")
            print("Email already exist")
            return redirect('/')
        else:
            user=User(name=name,email=email,password=password,address=address)
            user.save()

    return render(request,"home.html",{'alluser':alluser})

def detail(request):
    user=User.objects.all()
    return render(request,"detail.html",{'user':user})

def delete(request,userid):
    user=User.objects.get(id=userid)
    user.delete()
    return redirect('home')

def update(request,id):
    user=User.objects.get(id=id)
    editform=UserForm(request.POST or None, instance=user)
    if editform.is_valid():
        editform.save()
        return redirect('/')
    return render(request,"edit.html",{'user':user,'f':editform})

