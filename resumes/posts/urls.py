from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('group/<slug:slug>/', views.all_group, name='group_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('create/', views.resume_create, name='resume'),
    path('posts/<int:post_id>/detail/', views.resume_detail, name='resume_detail'),
    path('posts/<int:post_id>/edit/', views.resume_edit, name='resume_edit'),
    path('posts/<int:post_id>/delete/', views.resume_delete, name='resume_delete'),
    path('', views.index, name='index'),
]