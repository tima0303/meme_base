from django.shortcuts import render, redirect

from meme.forms import MemeForm


def manage(request):
    """
    Фун-я перенаправляющая на страницу управления мемами
    :param request:
    """
    data = {
        'title': 'Управление мемами'
    }
    return render(request, 'meme/manage.html', data)


def bookmarks(request):
    """
    Фун-я перенаправляющая на страницу закладок
    :param request:
    """
    data = {
        'title': 'Закладки'
    }
    return render(request, 'meme/bookmarks.html', data)


def create(request):
    """
    Фун-я перенаправляющая на форму по добавлению мема
    :param request:
    """
    error = ''
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверно заполнена'

    form = MemeForm()
    data = {
        'title': 'Форма по добавлению мема',
        'form': form,
        'error': error

    }
    return render(request, 'meme/create.html', data)