from django.urls import path
from .views import SignUpView, LoginUser, LogoutUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', SignUpView.as_view(), name='registration'),
    path('', LoginUser.as_view(), name='entrance'),
    path('logout', LogoutUser, name='logout')
]