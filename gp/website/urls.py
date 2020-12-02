from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_details/<slug>', views.portfolio, name='portfolio_details'),
]
