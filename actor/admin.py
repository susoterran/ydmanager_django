from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_jpn', 'name_eng', 'create_date')
    list_filter = ('name',)
    search_fields = ('name', 'name_jpn', 'name_eng')
    #prepopulated_fields = {'slug': ('number',)}