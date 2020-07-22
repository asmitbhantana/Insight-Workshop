from django.shortcuts import get_object_or_404
from django.urls import path
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from Article.models import ArticleItem
from .forms import DashboardArticleForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@method_decorator(login_required, name='dispatch')
class DashboardListArticleView(ListView):
    template_name = 'Dashboard/dashboard.html'
    model = ArticleItem

    def get_queryset(self):
        print("User", self.request.user)
        return ArticleItem.objects.filter(author=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update({'category_list': Category.objects.all()})
        print(context)
        return context


@method_decorator(login_required, name='dispatch')
class ArticleFormView(FormView):
    template_name = 'Dashboard/add-article.html'
    form_class = DashboardArticleForm
    success_url = reverse_lazy('dashboard:index')

    def get_queryset(self):
        return ArticleItem.objects.filter(
            author=self.request.user
        )

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ArticleUpdateView(UpdateView):
    template_name = 'Dashboard/add-article.html'
    form_class = DashboardArticleForm
    success_url = reverse_lazy('dashboard:index')

    context_object_name = 'pki'

    def get_queryset(self):
        return ArticleItem.objects.filter(
            author=self.request.user
        )


@method_decorator(login_required, name='dispatch')
class ArticleDeleteView(DeleteView):
    model = ArticleItem
    success_url = reverse_lazy('dashboard:index')

    def get_queryset(self):
        return ArticleItem.objects.filter(
            author=self.request.user
        )

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
