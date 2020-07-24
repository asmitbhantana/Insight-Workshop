from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm

User = get_user_model()


# Create your views here.
def login_view(request):
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect('account:profile')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user:
                print("User exists", user)
                login(request, user)
                return redirect('blog:index')
            else:
                form.add_error('email', "Error On Credentials")
                print("Auth credentials doesn't matches")
            print("Valid Form")
        print(request.POST)
    elif request.method == 'GET':
        pass
        # form = LoginForm()
    return render(request, 'Accounts/login.html', {'form': form})


def profile_view(request):
    if request.user.is_authenticated:
        # this is passed fot a context a[[
        # from statusapp.models import StatusMessage
        # messages = StatusMessage.objects.filter(user=request.user)
        return redirect(reverse_lazy('blog:index'))
    else:
        return redirect(reverse_lazy('account:login'))


def logout_view(request):
    logout(request)
    return redirect('blog:index')


#
def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print("Valid data")
            cleaned_data = register_form.cleaned_data
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
            new_user.set_password(cleaned_data['password'])
            new_user.save()

            return redirect('account:login')
        else:
            print("invalid data")
            # cleaned_data = register_form.cleaned_data
            # print(request.POST)

    elif request.method == 'GET':
        register_form = RegisterForm()

    return render(request, 'Accounts/register.html',
                  {
                      'form': register_form,
                  })


def invalid(request):
    return render(request, 'Accounts/invalid_token.html')
