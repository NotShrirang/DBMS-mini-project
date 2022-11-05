from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_page, name='add'),
    path('add/steps', views.create_recipe1, name='add_steps'),
    path('add/create_recipe', views.create_recipe2, name='create_recipe'),
]
