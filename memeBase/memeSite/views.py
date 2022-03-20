from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Meme


def index(request):
    """
    Фун-я перенаправляющая на галвную страницу
    :param request:
    """
    meme = Meme.objects.order_by('-time_create')
    return render(request, 'memeSite/index.html', {'meme': meme})


def guide(request):
    """
    Фун-я перенаправляющая на страницу помощи
    :param request:
    """
    data = {
        'title': 'Помощь'
    }
    return render(request, 'memeSite/guide.html', data)


def authorization(request):
    """
    Фун-я перенаправляющая на страницу входа
    :param request:
    """
    data = {
        'title': 'Вход'
    }
    return render(request, 'memeSite/authorization.html', data)


def pageNotFound(request, exception):
    """
    Обработчик неверно заданного адреса
    :param request:
    :param exception:
    :return:
    """
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
