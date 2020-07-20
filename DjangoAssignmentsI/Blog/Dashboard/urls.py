from django.urls import path
from .views import DashboardListArticleView, ArticleFormView, ArticleDeleteView, ArticleUpdateView

app_name = 'dashboard'
urlpatterns = [
    path('index/', DashboardListArticleView.as_view(), name='index'),
    path('add/', ArticleFormView.as_view(), name='add'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]
