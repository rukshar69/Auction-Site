from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, CustomUserCreationForm,  CustomAuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required
def index(request):

    return render(request, 'core/index.html')


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Get the email from the form data
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)  # Authenticate using email and password
            if user is not None:
                login(request, user)
                return redirect('core:index')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('/login/')
#     else:
#         form = SignupForm()

#     return render(request, 'core/signup.html', {
#         'form': form
#     })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Set the username as the email
            user.save()
            #login(request, user)
            return redirect('core:login')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('core:login')