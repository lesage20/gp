from django.forms import ModelForm
from website.models import ContactForm, Newsletter



class FormForContact(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
        
class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']