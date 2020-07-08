from django.contrib import admin
from .models import Authors, Books, Languages, Publishers, Series, Tags
# Register your models here.

@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (["name"])

@admin.register(Languages)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (["id", "lang_code"])

@admin.register(Publishers)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (["id","name"])

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = (["id","name"])

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = (["id","name"])

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = (["id","title", "author_sort"])