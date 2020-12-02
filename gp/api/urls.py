from django.urls import path, include
from .views import *



from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('presentations', PresentationViewSet)
router.register('about', AboutViewSet)
router.register('siteInfo', SiteInfoViewSet)
router.register('contact', ContactViewSet)
router.register('contactForm', ContactFormViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('team', TeamViewSet)
router.register('portfolio', PortfolioViewSet)
router.register('service', ServiceViewSet)
router.register('hero', HeroViewSet)
router.register('count', CountViewSet)
router.register('client', ClientViewSet)
router.register('cta', CtaViewSet)
router.register('testimonial', TestimonialViewSet)
router.register('feature', FeatureViewSet)

urlpatterns = [
    
]
urlpatterns += router.urls

