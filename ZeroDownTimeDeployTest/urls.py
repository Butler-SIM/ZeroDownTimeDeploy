
from django.contrib import admin
from django.urls import path

from ZeroDownTimeDeployTest.views import main

app_name = 'ZeroDownTimeDeployTest'

urlpatterns = [
    path('', main, name='main'),

]
