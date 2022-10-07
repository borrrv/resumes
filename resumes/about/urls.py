from django.urls import path, include
from . import views

app_name = 'about'
urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='author')
]
