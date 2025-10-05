from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline','count_views')
    list_filter = ('headline','count_views')
    search_fields = ('headline', 'content',)