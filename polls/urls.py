from django.urls import path

from . import views

urlpatterns = [
    path('create_quest/', views.create_quest, name='create_quest'),
    path('get_quest/', views.get_quest, name='get_quest'),
    path('delete_quest/', views.delete_quest, name='delete_quest'),
    path('update_quest/', views.update_quest, name='update_quest'),
    path('create_choice/', views.create_choice, name='create_choice'),
    path('get_choice/', views.get_choice, name='get_choice'),
    path('update_choice/', views.update_choice, name='update_choice'),
    path('delete_choice/', views.delete_choice, name='delete_choice'),
]
