from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message


# Create your views here.

def contact_form(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        success = True,
        message = 'İletişim formu başarıyla gönderildi!'

    else:
        success = False
        message = 'Önerilen yöntem geçerli değil.'

    Message.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message,
    )

    context = {
        'success': True,
        'message': 'İletişim formu başarıyla gönderildi!'
    }
    return JsonResponse(context)

def contact(request):
    return render(request, 'contact.html')