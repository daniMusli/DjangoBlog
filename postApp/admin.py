from django.contrib import admin
from .models import post
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_display_links = ['date']
    list_filter = ['date']
    search_fields = ['title','content']
    list_editable = ['title']


    class Meta:
        model = post

admin.site.register(post,postAdmin)
