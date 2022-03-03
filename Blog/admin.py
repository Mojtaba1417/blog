from django.contrib import admin
from Blog.models import post

# Register your models here.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    search_fields = ('title','body')
    list_filter = ('status','publish','created','author')

