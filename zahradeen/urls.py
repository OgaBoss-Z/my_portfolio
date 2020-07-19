from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import ProjectDetailView

urlpatterns = [
    path('', views.home, name='home-page' ),
    #path('<pk>/<slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('<pk>/<slug>/', views.project_detail, name='project-detail'),

]


