from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'memeSite/index.html', data)


def guide(request):
    data = {
        'title': 'Помощь'
    }
    return render(request, 'memeSite/guide.html', data)


def authorization(request):
    data = {
        'title': 'Вход'
    }
    return render(request, 'memeSite/authorization.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
