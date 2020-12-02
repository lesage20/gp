
from rest_framework import viewsets 
from rest_framework.response import Response 
from website.models import * 
from .serializers import  *

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer 
    queryset = Category.objects.all()


class PresentationViewSet(viewsets.ModelViewSet):
    serializer_class = PresentationSerializer 
    queryset = Presentation.objects.all()


class SiteInfoViewSet(viewsets.ModelViewSet):
    serializer_class = SiteInfoSerializer 
    queryset = SiteInfo.objects.all()


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer 
    queryset = About.objects.all()

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer 
    queryset = Contact.objects.all()

class ContactFormViewSet(viewsets.ModelViewSet):
    serializer_class = ContactFormSerializer 
    queryset = ContactForm.objects.all()

class NewsletterViewSet(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer 
    queryset = Newsletter.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer 
    queryset = Team.objects.all()

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer 
    queryset = Portfolio.objects.all()

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer 
    queryset = Service.objects.all()

class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer 
    queryset = Hero.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer 
    queryset = Client.objects.all()

class CountViewSet(viewsets.ModelViewSet):
    serializer_class = CountSerializer 
    queryset = Count.objects.all()

class FeatureViewSet(viewsets.ModelViewSet):
    serializer_class = FeatureSerializer 
    queryset = Feature.objects.all()

class CtaViewSet(viewsets.ModelViewSet):
    serializer_class = CtaSerializer 
    queryset = Cta.objects.all()

class TestimonialViewSet(viewsets.ModelViewSet):
    serializer_class = TestimonialSerializer 
    queryset = Testimonial.objects.all()



