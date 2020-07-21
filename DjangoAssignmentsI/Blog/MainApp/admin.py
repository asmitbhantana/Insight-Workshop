from django.contrib import admin
from Article.models import ArticleItem, Category
# Register your models here.

admin.site.register(ArticleItem)
admin.site.register(Category)
