from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'info', 'create_date')
    list_filter = ('name',)
    search_fields = ('name', 'info')
    #prepopulated_fields = {'slug': ('number',)}