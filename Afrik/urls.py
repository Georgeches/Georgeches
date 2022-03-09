from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('members/', views.members, name="members"),
    path('notifications/', views.notifications, name="notifications"),
    path('posts/', views.posts, name="posts"),
    path('profile/', views.profile, name="profile")
]