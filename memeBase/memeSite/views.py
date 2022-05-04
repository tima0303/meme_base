from django.http import HttpResponseNotFound

from django.shortcuts import render
from django.views.generic import ListView

from meme.models import Meme


class MemeHome(ListView):
    model = Meme
    template_name = "memeSite/index.html"
    context_object_name = "meme"


class SearchResultView(ListView):
    model = Meme
    template_name = "memeSite/search_results.html"
    context_object_name = "meme"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Meme.objects.filter(title__icontains=query)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ищем мемы'
        return context


def guide(request):
    """
    Фун-я перенаправляющая на страницу помощи
    :param request:
    """
    data = {
        'title': 'Помощь'
    }
    return render(request, 'memeSite/guide.html', data)


def pageNotFound(request, exception):
    """
    Обработчик неверно заданного адреса
    :param request:
    :param exception:
    :return:
    """
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
