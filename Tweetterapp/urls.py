from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import TweetCreateView


urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('profileupdate', views.profileupdate, name='profileupdate'),
    path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('create/', TweetCreateView.as_view(), name='tweetcreate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
