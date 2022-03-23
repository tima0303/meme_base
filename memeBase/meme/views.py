from django.shortcuts import render


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

