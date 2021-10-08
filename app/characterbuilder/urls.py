from django.urls import path

from .views import HomePageView

app_name = 'characterbuilder'

urlpatterns = [
    path('characterbuilder/', HomePageView.as_view(), name='homepage'),
]