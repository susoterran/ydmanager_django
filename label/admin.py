from django.contrib import admin
from .models import Label

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'create_date', 'tag_list')
    list_filter = ('create_date',)
    search_fields = ('number', 'info')
    #prepopulated_fields = {'slug': ('number',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obh.tags.all())