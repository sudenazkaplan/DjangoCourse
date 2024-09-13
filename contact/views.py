from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message
from contact.forms import ContactForm


# Create your views here.

def contact_form(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            contact_form.send_mail()

            success = True
            message = 'İletişim formu başarıyla gönderildi!'
        else:
            success = False
            message = 'İletişim formu geçerli değil.'

    else:
        success = False,
        message = 'Önerilen yöntem geçerli değil.'

    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)


def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)
