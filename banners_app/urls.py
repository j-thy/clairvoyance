from django.urls import path
from .views import *

urlpatterns = [
    path("", example_view, name="example"),
    # 1. Server gets a URL request for clairvoyance.dev/events
    # EventView is called 
    path('events/', EventView.as_view(), name='events'),
]
