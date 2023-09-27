from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from .models import Item

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html', {'user_info': request.user})

@login_required
def adjust_amount(request, item_id, action):
    item = get_object_or_404(Item, id=item_id)
    if action == 'add':
        item.amount += 1
    elif action == 'subtract':
        item.amount -= 1
        if item.amount < 0:
            item.amount = 0
    item.save()
    return redirect('home')

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('home')

