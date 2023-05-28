# social_platform/urls.py

from django.urls import path
from social_app import views

urlpatterns = [
    # Other URL patterns
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('connect/<int:user_id>/', views.connect, name='connect'),
    path('create_post/', views.create_post, name='create_post'),
    path('search/', views.search, name='search'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('connection_profile/<int:user_id>/', views.connection_profile, name='connection_profile'),
]

