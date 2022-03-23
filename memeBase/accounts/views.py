from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def authorization(request):
    """
    Фун-я перенаправляющая на страницу авторизации
    :param request:
    """
    data = {
        'title': 'Авторизация'
    }
    return render(request, 'accounts/authorization.html', data)


def personal(request):
    """
    Фун-я перенаправляющая в личный кабинет пользователя
    :param request:
    """
    data = {
        'title': 'Мой профиль',
    }
    return render(request, 'accounts/personal.html', data)


def settings(request):
    """
    Фун-я перенаправляющая в личный кабинет пользователя
    :param request:
    """
    data = {
        'title': 'Настройки профиля'
    }
    return render(request, 'accounts/settings.html', data)