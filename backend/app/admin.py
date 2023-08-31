from django.contrib import admin
from .models import Words


# Register your models here.
class WordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gender', 'word']
    list_editable = ['gender', 'word']


admin.site.register(Words, WordAdmin)
