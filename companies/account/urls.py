
from django.urls import path
from .views import log,reg 

urlpatterns=[
    path('login/',log),
    path('registration/',reg),
]    