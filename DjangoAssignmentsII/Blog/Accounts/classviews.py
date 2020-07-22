from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .classform import UserLoginForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'Accounts/login.html'
    success_url = reverse_lazy('blog:index')

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        print(context)
        return context

    def form_valid(self, form):
        user = authenticate(email=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
        else:
            form.add_error('email', "Error On Credentials")
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('blog:index')
