from django.urls import path
from app1.views import *

app_name = 'kushal'

urlpatterns = [
    path('home/', home, name='contact_me'),
]