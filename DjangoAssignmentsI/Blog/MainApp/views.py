from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Article.models import ArticleItem, Category
from django.contrib.auth import get_user_model


# Create your views here.

class ListCourses(ListView):
    template_name = 'MainApp/landing.html'
    model = ArticleItem
    ordering = '-created_date'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'category_list': Category.objects.all()})
        print(context)
        return context


class ShowDetail(DetailView):
    model = ArticleItem
    template_name = 'MainApp/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        author_obj = context['object'].author
        author_text = author_obj.username + " wrote this article. Mail him at " + author_obj.email + " for further query."
        context.update({'author_text': author_text})
        return context
