from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.sign_up, name = "signup"),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home, name = "home"),
    path('posts/', views.create_post, name = "posts"),
    path('mypost/<int:id>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/edit/', views.edit_post, name = "post-edit"),
    path('post/<int:id>/delete/', views.delete_post, name = "post-delete"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    
]