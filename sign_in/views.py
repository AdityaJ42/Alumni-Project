from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Register, ProfileForm
from django.contrib.auth import login, authenticate
from .filters import findUser
from .models import Profile
from events.models import Events
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    event_list = Events.objects.all().order_by('-id')[:10:1]
    return render(request, 'sign_in/home.html',{'events': event_list})

def register(request):
    registered = False
    if request.method == "POST":
        user_form = Register(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            login(request, authenticate(username=username, password=raw_password))
            registered = True
    else:
        user_form = Register()
        profile_form = ProfileForm()
    if registered:
        return redirect('/')
    else:
        return render(request, 'sign_in/register.html', {'user_form': user_form, 'profile_form': profile_form})

def search(request):
    # user = User.objects.get(username=request.username)
    profile = Profile.objects.all()
    user_filter = findUser(request.GET, queryset=profile)
    return render(request, 'sign_in/search.html', {'filter': user_filter})

def profile(request):
    user = request.user
    profile = Profile.objects.get(user=request.user)
    return render(request, 'sign_in/profile.html', {'user': user, 'profile': profile})
