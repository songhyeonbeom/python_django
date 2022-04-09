# Register your models here.
from django.contrib import admin
from insta.models import Album, Photo, Answer


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'slug',)
    search_fields = ['name']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'image', 'upload_dt',)
    search_fields = ['id', 'image', ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'create_date', 'owner', 'modify_date',]
    list_display_links = ['id', ]
    search_fields = ['content', ]


