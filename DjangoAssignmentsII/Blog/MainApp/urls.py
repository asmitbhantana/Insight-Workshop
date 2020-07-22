from django.urls import path

from .views import ListCourses,ShowDetail

app_name = 'blog'
urlpatterns = [
    path('landing/', ListCourses.as_view(), name="index"),
    path('detail/<int:pk>/', ShowDetail.as_view(), name="detail"),
]
