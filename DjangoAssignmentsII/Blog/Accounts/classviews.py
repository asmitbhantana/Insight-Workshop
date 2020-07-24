from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView
from django.urls import reverse_lazy
from .classform import UserLoginForm, UserSignupForm
from django.views.generic import View
from Blog.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator

User = get_user_model()
account_activation_token = PasswordResetTokenGenerator()


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


class UserSignupView(FormView):
    form_class = UserSignupForm
    template_name = 'Accounts/register.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        # profile_image = request.FILES['profile_image']
        # if profile_image.name.endswith(".jpeg") or profile_image.name.endswith(
        #         '.jpg') or profile_image.name.endswith(".png"):
        #     fs = FileSystemStorage()
        #     filename = fs.save(profile_image.name, profile_image)
        # print("File name is", filename)
        new_user = User(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'],
                        email=cleaned_data['email'], username=cleaned_data['username'], is_active=False)
        print("User is", new_user)
        new_user.save()
        new_user.set_password(cleaned_data['password1'])
        new_user.save()

        current_site = get_current_site(self.request)
        subject = 'Activate Your Asmit Blogs Account'
        message = render_to_string('Accounts/account_activation_email.html', {
            'user': new_user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
            'token': PasswordResetTokenGenerator.make_token(self=account_activation_token, user=new_user),
        })
        send_mail(subject, message, EMAIL_HOST_USER, [new_user.email], fail_silently=False)
        messages.success(self.request, 'Please Confirm your email to complete registration.')

        return redirect('account:login')


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and PasswordResetTokenGenerator.check_token(self=account_activation_token, user=user,
                                                                        token=token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, 'Your account have been confirmed.')
            return redirect('account:login')
        else:
            return redirect('account:invalid')
