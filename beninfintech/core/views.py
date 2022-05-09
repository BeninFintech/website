from django.shortcuts import render


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
    return render(request, 'core/contact.html')
