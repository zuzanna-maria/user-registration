from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import CustomUser
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    user = get_user_model()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()

        #     user = CustomUser.objects.create_user(
        #     email='email',
        #     username='username',
        #     password='password',
        #     first_name='first_name',
        #     last_name='last_name',
        #     date_of_birth='2006-10-10',
        #     school='school'
        # )
            form.save()
            # user.save()

            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
