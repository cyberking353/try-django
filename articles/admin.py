from django.contrib import admin
from .models import Article
# Register your models here.
# added this comment for testing
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    search_fields = ['id','title',]

admin.site.register(Article, ArticleAdmin)
