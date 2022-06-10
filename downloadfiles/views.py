from pdb import pm
from subprocess import PIPE
from wsgiref.simple_server import sys_version
from anyio import run
from django.shortcuts import render
# Create your views here.
#import sys
#import spacy
# import Pdf_extract_cleaning as pec
#from scripts import Pattern_Matching as pm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import ResumeUpload, KeywordUpload
from .models import UploadPdf

def base(request):
    return render(request, "downloadfiles/base.html")
def post_detail(request):
    return render(request, "downloadfiles/post_detail.html")

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'downloadfiles/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'downloadfiles/home.html'   
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'downloadfiles/about.html', {'title': 'About'})

#def store_pdf(request):
#     uploadpdf = UploadPdf.objects.all()
#     return render(request, 'notmatik/store_pdf.html', {'uploadpdf': uploadpdf})

#run(sys_version.executable,['//scripts//pdf_extract_cleaning.py'], shell = False,stdout=PIPE)


def upload_pdf(request):
    if request.method == "POST":
        form = ResumeUpload(request.POST, request.FILES)
        files = request.FILES.getlist('resumes')
        if form.is_valid():
            for f in files:
                file_instance = UploadPdf(resumes=f)
                file_instance.save()
        #pec.main()
        return redirect('upload_keyword')
    else:
        form = ResumeUpload()
    return render(request, 'downloadfiles/upload_pdf.html', {'form': form})

def upload_keyword(request):
    if request.method == "POST":
        form = KeywordUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = KeywordUpload()
    data = pm.main()
    return render(request, 'downloadfiles/upload_keyword.html', {'form': form, 'df':data.to_html(classes='table table-striped table-hover', index=False, render_links=True, escape=False)})