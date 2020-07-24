from django.urls import path

from .views import login_view, profile_view, register_view, logout_view, invalid
from .classviews import UserLoginView, UserLogoutView, UserSignupView, ActivateAccount

app_name = "account"

urlpatterns = [
    # path('login/', login_view, name="login"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', profile_view, name="profile"),
    path('register/', UserSignupView.as_view(), name="register"),
    # path('register/', register_view, name="register"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    # path('logout/', logout_view, name="logout"),

    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

    path('invalid/', invalid, name="invalid")

]
