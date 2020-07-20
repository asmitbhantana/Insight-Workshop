from django.forms import ModelForm
from django import forms
from Article.models import ArticleItem
from ckeditor.widgets import CKEditorWidget


class DashboardArticleForm(ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    banner = forms.ImageField()
    class Meta:
        model = ArticleItem
        fields = ['title', 'description', 'banner', 'category', 'tags']
