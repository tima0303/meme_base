from django.shortcuts import render, redirect, get_object_or_404

from meme.forms import MemeForm

from django.views.generic import DetailView

from meme.models import Meme


class MemeDetailView(DetailView):
    model = Meme
    template_name = 'meme/details_view.html'
    context_object_name = 'meme'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['fav'] = Meme.objects.order_by().values('tag').distinct()
    #     return context


# def meme_detail_view(request, id):
#     meme = get_object_or_404(Meme, status='is_published')
#     fav = bool
#     if meme.favorites.filter(id=request.user.id).exists():
#         fav = True
#     return render(request, 'meme/details_view.html', {'meme': meme, 'fav': fav})


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
    return render(request, 'meme/favorites.html', data)


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
