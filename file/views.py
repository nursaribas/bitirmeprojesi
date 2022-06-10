from msilib.schema import ListView
from os import name
from queue import Empty
from sys import path_hooks
from django.shortcuts import redirect, render
from fastapi import Query
from pandas import describe_option
from .models import  Document, File
from .forms import DocumentForm, FileFieldForm, FileForm
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# uygulamamızdaki html sayfalarının görüntülenmesi
def filelist(request):
    return render(request,"file/filelist.html")

def file(request):
    filelist = File.objects.all()
    query = request.GET.get('q')
    if query:
        filelist= filelist.filter(name__icontains=query)
    paginator = Paginator(filelist,5)

    page = request.GET.get('sayfa')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return render(request,"file/file.html", {'files':files})   



def showfile(request):

    lastfile= File.objects.last()
                                                 
    filepath = lastfile.filepath('./media/files.pdf')            

    filename= lastfile.filename

    description = lastfile.description

    publishing_date= lastfile.publishing_date


    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        context= {'filepath': filepath,
                   'form': form,
                   'filename': filename,
                   'description': description,
                   'publishing_date': publishing_date
                  }
    
      
    return render(request, 'file/file.html', context)


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file/upload.html', 
        {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file/file.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = DocumentForm()
    return render(request, 'file/model_form_upload.html',
    {
        'form': form
    })

def success(request):
    file = File.objects.order_by('name')
    return render(request, "file/success.html", 
    {
        "file": file
    })



class FileFieldFormView(FormView):
     form_class = FileFieldForm
     template_name = 'upload.html' 
success_url = 'filelist.html'  

def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

#class filelist(ListView):
#    model = File
#    def get_queryset(self, *args, **kwargs):
#        qs = super(file_list, self).get_queryset(*args, **kwargs)
#        qs = qs.order_by("-id")
#        return qs
#File.objects.filter(published_date__lte=timezone.now()).order_by('publishing_date')
#File.objects.filter(name,describe_option)



#def filelist(request):
    #files = File.objects.filter(name,publishing_date)
#    return render(request, 'file/filelist.html', {'posts': files})
