from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class ArticleItem(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    banner = models.ImageField(default='default.jpeg')
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title


