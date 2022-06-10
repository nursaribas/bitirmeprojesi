
from multiprocessing import context
from django.shortcuts import render



# html sayfalarımızın görüntülenmesi

def index(request):
    return render(request, "notmatik/index.html")
def menu_cıkıs(request):
    return render(request, "notmatik/index.html")
def akademisyen(request):
    return render(request, "notmatik/akademisyen.html")
def egitim(request):
    return render(request, "notmatik/egitim.html")
def fen(request):
    return render(request, "notmatik/fen.html")
def ibf(request):
    return render(request, "notmatik/ibf.html")
def ilahiyat(request):
    return render(request, "notmatik/ilahiyat.html")
def muhendislik(request):
    return render(request, "notmatik/muhendislik.html")
def tıp(request):
    return render(request, "notmatik/tıp.html")
def insaatmuh(request):
    return render(request, "notmatik/insaatmuh.html")
def makinemuh(request):
    return render(request, "notmatik/makinemuh.html")
def bilgisayarmuh(request):
    return render(request, "notmatik/bilgisayarmuh.html")
def elektrikmuh(request):
    return render(request, "notmatik/elektrikmuh.html")
def fakulte(request):
    return render(request, "notmatik/fakulte.html")
def iletisim(request):
    return render(request, "notmatik/iletisim.html")


def menu(request):
    return render(request, "notmatik/menu.html")
