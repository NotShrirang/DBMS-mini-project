from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit', views.load_edit_recipe, name='edit'),
    path('update', views.update, name='update'),
    path('remove', views.remove, name='remove')
]