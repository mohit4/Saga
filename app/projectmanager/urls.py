from django.urls import path

from .views import ProjectCreateView, ProjectUpdateView, ProjectListView, ProjectDetailView, ProjectDeleteView

app_name = 'projectmanager'

urlpatterns = [
    path('project/all/', ProjectListView.as_view(), name='project-list' ),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail' ),
    path('project/create/', ProjectCreateView.as_view(), name='project-create' ),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update' ),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete' ),
]