from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import User, Connection


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Process the signup data and create a new user
            user = User(name=name, mobile=mobile, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'social_app/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            user = authenticate(request, mobile=mobile, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid mobile or password.')
    else:
        form = LoginForm()
    
    return render(request, 'social_app/login.html', {'form': form})

def connect(request, user_id):
    if request.method == 'POST':
        from_user = request.user
        to_user = User.objects.get(id=user_id)
        connection = Connection(from_user=from_user, to_user=to_user)
        connection.save()
        return redirect('search_results')
    else:
        # Render the page with a form to select users to connect with
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'social_app/connect.html', {'users': users})


# social_app/views.py

def create_post(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST['content']
        visibility = request.POST['visibility']
        post = post(user=user, content=content, visibility=visibility)
        post.save()
        return redirect('home')
    else:
        return render(request, 'social_app/create_post.html')

    
    return render(request, 'social_app/create_post.html', {'form': form})




def search(request):
    query = request.GET.get('q')
    users = User.objects.filter(name__icontains=query)
    return render(request, 'social_app/search_results.html', {'users': users})



def user_profile(request):
    connected_users = request.user.connections.all()
    return render(request, 'social_app/user_profile.html', {'connected_users': connected_users})


def connection_profile(request, user_id):
    user = User.objects.get(id=user_id)
    connections = user.connections.all()
    mutual_connections = connections.filter(from_user=request.user)
    return render(request, 'social_app/connection_profile.html', {'connections': connections, 'mutual_connections': mutual_connections})
