from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from blog.models import Blogpost


# Create your views here.
def index(request):
    return render(request,"index.html")

def loginview(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request, user)
                return redirect('user')
            
            else:
                messages.warning(request, 'invalid credentials')
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
            messages.warning(request, "Invalid Credentials")
    return render(request, 'loginview.html', {'form': form, 'msg': msg})

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            messages.success(request,'your account is created successfully')
            return redirect('loginview')
        else:
            messages.warning(request, form.errors)
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Loged out")
    return redirect('index')

def user(request):
    posts = Blogpost.objects.filter(is_completed=False)
    context = {"posts": posts}
    return render(request,"user.html",context)
def patient(request):
    return render(request,"patient.html")
    