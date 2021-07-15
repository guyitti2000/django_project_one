from django.urls import path

from . import views
# . means same file path as previous one

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
]
