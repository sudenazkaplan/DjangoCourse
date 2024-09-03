from tkinter import Image

from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Create your views here.

def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    # Images
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file

    social_medias = SocialMedia.objects.all()
    documents = Document.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'social_medias': social_medias,
        'documents': documents,
    }

    return render(request, 'index.html', context=context)


def contact(request):
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    context = {
        'about_myself_footer': about_myself_footer,
    }

    return render(request, 'contact.html', context=context)


def about(request):
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    # Skills
    skills = Skill.objects.all().order_by('order')

    # experience
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')

    context = {
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }

    return render(request, 'about-us.html', context=context)


def portfolio(request):
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter

    context = {
        'about_myself_footer': about_myself_footer,
    }

    return render(request, 'portfolio.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)
