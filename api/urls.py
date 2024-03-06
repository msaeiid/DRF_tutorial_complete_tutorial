from django.urls import path, include

from api import views

urlpatterns = [
    path('home/', views.api_home, name='api_home'),
]
