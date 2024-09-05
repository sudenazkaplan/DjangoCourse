from tkinter import Image

from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Create your views here.

def get_general_setting(parameter):
    try:
        obj = about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter
    except:
        obj = ''

    return obj

def get_image_setting(parameter):
    try:
        obj = site_favicon = ImageSetting.objects.get(name='site_favicon').file
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
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter

    # Images
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file

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
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter

    # Skills
    skills = Skill.objects.all().order_by('order')

    # experience
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')

    context = {
        'about_myself_welcome': about_myself_welcome,
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
