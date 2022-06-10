from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url, include
from . import views

#uygulamada yer alan html sayfaları
urlpatterns = [
    path('menu/file/', views.file, name='file'),
    path('menu/filelist/', views.filelist, name='filelist'),
    path('menu/model_form_upload/', views.model_form_upload, name='model_form_upload'),
    path('upload/', views.upload, name= 'upload'),
    path('menu/showfile/',views.showfile,name='showfile'),
    path('menu/post/',views.post,name='post'),
    path('success/',views.success,name='success'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
