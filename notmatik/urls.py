"""notmatik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from downloadfiles.views import PostDetailView
from user import views as user_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from downloadfiles import views as downloadfiles_view
from file import views as file_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notmatikbitirme.urls')),
    path('user/', include('user.urls')),
    path('file/', include('file.urls')),
    path('downloadfiles/', include('downloadfiles.urls')),

    ##### USERla ilgili yol ##########################
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name ='logout'),
    path('register/', user_view.register, name ='register'),
    path('menu/profile/', user_view.profile, name ='profile'),
    path('email/', user_view.email, name ='email'),
    path('accounts/login/', user_view.login, name='login'),


    ### FİLE ilgili yol ###
    path('menu/file/', file_view.file, name='file'),
    path('menu/model_form_upload/', file_view.model_form_upload, name='model_form_upload'),
    path('upload', file_view.upload, name= 'upload'),
    path('menu/filelist/', file_view.filelist, name='filelist'),
    path('menu/showfile/', file_view.showfile, name='showfile'),
    path('menu/success/', file_view.success, name='success'),
    path('menu/post/', file_view.post, name='post'),


    ##  DOWNLOADFİLES####
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('base/',downloadfiles_view.base, name = 'base'),
    path('about/', downloadfiles_view.about, name='about'),
    path('uploadpdf/', downloadfiles_view.upload_pdf, name='upload_pdf'),
    path('keyword/', downloadfiles_view.upload_keyword, name='upload_keyword'),
    path('home/',downloadfiles_view.home, name='home'),

    
]  + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
