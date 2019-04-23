from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersFormView, name="users"),
]
