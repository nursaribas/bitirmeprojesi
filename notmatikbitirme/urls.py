from django.urls import path
from . import views


#html sayfalarının url sinin belirlenmesi
urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('menu/akademisyen/', views.akademisyen, name="akademisyen"),
    path('menu/egitim/', views.egitim, name="egitim"),
    path('menu/fen/', views.fen, name="fen edebiyat"),
    path('menu/ibf/', views.ibf, name="ibf"),
    path('menu/ilahiyat/', views.ilahiyat, name="ilahiyat"),
    path('menu/muhendislik/', views.muhendislik, name="muhendislik"),
    path('menu/tıp/', views.tıp, name="tıp"),
    path('menu/insaatmuh/', views.insaatmuh, name="insaatmuh"),
    path('menu/makinemuh/', views.makinemuh, name="makinemuh"),
    path('menu/bilgisayarmuh/', views.bilgisayarmuh, name="bilgisayarmuh"),
    path('menu/elektrikmuh/', views.elektrikmuh, name="elektrikmuh"),
    path('menu/fakulte/', views.fakulte, name="fakulte"),
    path('menu/cıkıs/', views.menu_cıkıs, name="menucıkıs"),
    path('iletisim/', views.iletisim, name="iletisim"),

    
]