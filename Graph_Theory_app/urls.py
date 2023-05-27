from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index,name = 'index'),
    path("first/", views.first,name = 'first'),
    path('save_matrix_data', views.save_matrix_data, name='save_matrix_data'),
]