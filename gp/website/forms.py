from django.forms import ModelForm
from website.models import ContactForm



class FormForContact(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'