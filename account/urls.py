from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import SignUpView, LoginUser, LogoutUser, Profile, profile, ChangePasswordView, AppealCreateView, \
    AppealHistory
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', SignUpView.as_view(), name='registration'),
    path('', LoginUser.as_view(), name='entrance'),
    path('logout', LogoutUser, name='logout'),
    path('profile', Profile, name='profile'),
    path('profile-changed', profile, name='profile-changed'),
    path('password-change', ChangePasswordView.as_view(), name='password_change'),
    path('homepage/appeal', AppealCreateView.as_view(), name='appeal'),
    path('profile/appeal-history', AppealHistory.as_view(), name='appeal-history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)