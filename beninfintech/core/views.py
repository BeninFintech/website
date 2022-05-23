from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django_htmx.http import trigger_client_event

from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def institutions(request):
    return render(request, 'core/institutions-fin.html')


def solutions(request):
    return render(request, 'core/plateform.html')


def support(request):
    return render(request, 'core/support.html')


def materials(request):
    return render(request, 'core/materials.html')


def contact(request):
    if request.method == 'POST':
        post = request.POST
        if post.get('email'):
            # TODO Send Email to contact@bftgroup.co
            print('Sending ...')
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = f'BENIN FINTECH <{settings.EMAIL_HOST_USER}>'
            recipient_list = ['annyongdey19@gmail.com', 'myung.etouh@bftgroup.co']
            send_mail(subject, message, email_from, recipient_list)

            response = TemplateResponse(request, 'core/partials/contact-form.html')
            return trigger_client_event(
                response,
                "showAlert",
                {'success_message': 'Message envoyé'},
                after="swap",
            )

    return render(request, 'core/contact.html')
