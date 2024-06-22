from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]
