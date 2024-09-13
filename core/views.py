from tkinter import Image

from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Create your views here.

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj

def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''

    return obj


def layout(request):
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    about_myself_footer = get_general_setting('about_myself_footer')

    # Images
    site_favicon = get_image_setting('site_favicon')

    documents = Document.objects.all()
    social_medias = SocialMedia.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'documents': documents,
        'about_myself_footer': about_myself_footer,
        'site_favicon': site_favicon,
        'social_medias': social_medias,
    }
    return context

def index(request):
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')

    # Images
    home_banner_image = get_image_setting('home_banner_image')

    context = {
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'home_banner_image': home_banner_image,
    }

    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_welcome2 = get_general_setting('about_myself_welcome2')
    about_myself_welcome3 = get_general_setting('about_myself_welcome3')

    # Skills
    skills = Skill.objects.all().order_by('order')

    # experience
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')

    context = {
        'about_myself_welcome': about_myself_welcome,
        'about_myself_welcome2': about_myself_welcome2,
        'about_myself_welcome3': about_myself_welcome3,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }

    return render(request, 'about-us.html', context=context)


def portfolio(request):
    return render(request, 'portfolio.html')


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)
