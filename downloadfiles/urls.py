from django.urls import path
from downloadfiles.views import PostDetailView
from .views import (
    PostListView,
    PostDetailView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='resume-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('uploadpdf/', views.upload_pdf, name='upload_pdf'),
    path('keyword/', views.upload_keyword, name='upload_keyword'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    
]
