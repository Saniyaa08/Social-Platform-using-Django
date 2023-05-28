"""
URL configuration for social_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from social_app.views import signup
from social_app.views import login
from social_app.views import connect
from social_app.views import create_post
from social_app.views import search
from social_app.views import user_profile
from social_app.views import connection_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('connect/<int:user_id>/', connect, name='connect'),
    path('create_post/', create_post, name='create_post'),
    path('search/', search, name='search'),
    path('user_profile/', user_profile, name='user_profile'),
    path('connection_profile/<int:user_id>/', connection_profile, name='connection_profile'),

]
