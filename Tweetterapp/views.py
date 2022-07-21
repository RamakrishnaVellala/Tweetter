from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Tweet, Follower, Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    context = {'tweets': Tweet.objects.all}
    return render(request, 'Tweetterapp/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'Tweetterapp/register.html', context)


def Login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'Tweetterapp/login.html', {'form': form, 'title': 'log in'})


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def profile(request):
    return render(request, 'Tweetterapp/profile.html')


def profileupdate(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            return redirect('profile')
    else:
        pform = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'Tweetterapp/profileupdate.html', {'pform': pform})


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'Tweetterapp/create.html'
    fields = ['content', 'content_image']
    success_url = '/index'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
