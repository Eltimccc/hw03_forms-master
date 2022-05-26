# users/urls.py
# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import (
                                LoginView, 
                                LogoutView, 
                                PasswordResetView, 
                                PasswordResetDoneView, 
                                PasswordResetConfirmView, 
                                PasswordResetCompleteView,
                                )
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'signup/', views.SignUp.as_view(), 
        name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'password-reset/', 
        PasswordResetView.as_view(
        template_name='users/password_reset_form.html')),
    path(
        'password-reset/done/', 
        PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html')),
    path(
        'reset/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html')),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html')),
        ]  
