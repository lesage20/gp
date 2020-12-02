from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from django.http import HttpResponse
from .forms import OrderForm, CustomerForm, CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .mydecorators import anonymous, allowed_users, admin_only

from django.contrib import messages
# Create your views here.


def registerUser(request):
    form = CreateUser()
    
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid:
            try:
                user = form.save()
            except Exception as e:
                messages.error(request, f"{e}")
            else:
                
                login(request, user=user)
                username = form.cleaned_data.get('username')
                messages.success(request, f'+ Account {username} successfully  created')
                return redirect('index')
    
    
    datas={
        'form':form
    }
    return render(request, 'accounts/register.html', datas)


def loginUser(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Password or Username may be incorrect')
    
    
    datas = {
        
    }
    return render(request, 'accounts/login.html', datas)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    
    #customer = Customer.objects.get(id=pk)
    customer = Customer.objects.filter(user=request.user)[0]
    orders = Order.objects.filter(customer=customer)
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out For Delivery').count()
    
    print('userpage ', request.user.is_active)
    
    datas = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'out': out,
        'customer': customer
        
    }
    return render(request, 'accounts/user.html', datas)

def Usettings(request):
    customer= request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    
    
    datas = {
        'form': form,
    }
    return render(request, 'accounts/user-settings.html', datas)

