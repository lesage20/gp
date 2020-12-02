from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .forms import FormForContact, NewsletterForm
# Create your views here.

def index(request):
    
    print(dir(request))
    
    
    if request.method == 'POST':
        form = NewsletterForm()
        formulaire = FormForContact()
        if 'contact_sub' in request.POST:
            print('youpi')
            
            formulaire = FormForContact(request.POST)
            
            
            if formulaire.is_valid():
                formulaire.save()
                return redirect(request.path_info)
            else:
                return HttpResponse(f"Yako {formulaire.cleaned_data}")
        else:
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path_info)
            else:
                return HttpResponse(f"Yako {form.cleaned_data}")
                
            
        
            
            
    
    
    datas = {
        
    }
    return render(request, 'index.html', datas)

def portfolio(request, slug):
    pfolio = Portfolio.objects.get(slug=slug)
    
    form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        form = NewsletterForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            return redirect(request.path_info)
        else:    
            return HttpResponse('Veuillez verifier les information rentré')
    
    
    
    return render(request, "portfolio-details.html")

