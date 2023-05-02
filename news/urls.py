from django.urls import path
from .views import NewsView

urlpatterns = [
    path('homepage', NewsView.as_view(), name='homepage')
] 