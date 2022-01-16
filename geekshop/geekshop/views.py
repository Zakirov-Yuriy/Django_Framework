from django.shortcuts import render


def index(request):
    title = 'geekshop'

    context = {
        'title': title,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')
