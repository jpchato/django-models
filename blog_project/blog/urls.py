from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, ListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post_details/<int:pk>', HomePageView.as_view(), name='post_details' )

]
