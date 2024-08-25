from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about-us.html')

def portfolio(request):
    return render(request, 'portfolio.html')

