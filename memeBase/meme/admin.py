from django.contrib import admin

from django.contrib import admin

from .models import Meme


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
