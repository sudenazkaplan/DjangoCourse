from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message


# Create your views here.

def contact_form(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        success = True,
        message = 'İletişim formu başarıyla gönderildi!'

    else:
        success = False,
        message = 'Önerilen yöntem geçerli değil.'

    Message.objects.create(
        name = name,
        email = email,
        subject = subject,
        message = message,
    )

    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)

def contact(request):
    return render(request, 'contact.html')