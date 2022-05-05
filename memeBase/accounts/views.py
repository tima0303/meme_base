from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from meme.models import Meme
from .forms import UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def favorites_list(request):
    new = Meme.objects.filter(favorites=request.user)
    return render(request, 'meme/favorites.html', {'new': new})


@login_required
def favorites_add(request, id):
    meme = get_object_or_404(Meme, id=id)
    if meme.favorites.filter(id=request.user.id).exists():
        meme.favorites.remove(request.user)
    else:
        meme.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def settings(request):
    """
    Пользовательские настройки
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'accounts/settings.html', {'user_form': user_form})


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
