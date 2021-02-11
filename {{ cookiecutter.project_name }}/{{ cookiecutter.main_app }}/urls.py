from django.urls import path

from {{ cookiecutter.main_app }} import views

urlpatterns = [
    path('', views.index, name='home'),
]
