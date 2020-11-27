from django.urls import path

from . import views

urlpatterns = [
    path('', views.NamesListView.as_view(), name='index'),
    path(
        'names/<int:pk>', views.NamesDetailView.as_view(), name='name-detail'
    ),

    # API
    path('api/name/', views.create_sprintname, name='create-name'),
    path(
        'api/name/<int:sprint_id>', views.delete_sprintname, name='delete-name'
    ),
    path('api/names/search/<str:query>', views.search_sprintname, name='search-name')
]
