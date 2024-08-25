from django.urls import path
from .views import index, contact, about, portfolio

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('about-us/', about, name='about-us'),
    path('portfolio/', portfolio, name='portfolio'),
]
