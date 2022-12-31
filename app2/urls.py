from django.urls import path
from app2.views import *

app_name = 'joy'

urlpatterns = [
    path('info/', info, name='info'),
]