from django.urls import path

from . import views

#app_name = 'names'
urlpatterns = [
    path('', views.NamesListView.as_view(), name='index'),
    path('api/name/', views.create_sprintname, name='create-name'),
    path('api/name/<int:sprint_id>', views.delete_sprintname, name='delete-name'),
    path('names/<int:pk>', views.NamesDetailView.as_view(), name='name-detail'),
]
