from django.urls import path
from . import views

urlpatterns = [
    path('', views.whoami_view, name='whoami'),
]
