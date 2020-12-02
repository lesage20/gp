from django.shortcuts import render,redirect
from .models import *
from .forms import FormForContact
# Create your views here.

def index(request):
    
    form = FormForContact()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        form = FormForContact(request.POST)
        
        
        if form.is_valid():
            form.save()
            return redirect(request.path_info)

        
    
    
    datas = {
        
    }
    return render(request, 'index.html', datas)

def portfolio(request, slug):
    pfolio = Portfolio.objects.get(slug=slug)
    
    
    return render(request, "portfolio-details.html")

