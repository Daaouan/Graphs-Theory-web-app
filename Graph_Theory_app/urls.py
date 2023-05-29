from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,name = 'index'),
    path('save_matrix_data', views.save_matrix_data, name='save_matrix_data'),
    path("prim/", views.prim ,name = 'prim'),
    path("warshall/", views.warshall,name = 'warshall'),
    path("kruskal/", views.kruskal,name = 'kruskal'),
    path("dfs/", views.dfs,name = 'dfs'),
    path("bfs/", views.bfs,name = 'bfs'),
]