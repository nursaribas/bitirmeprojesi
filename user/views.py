from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


from user.forms import FileUpdateForm, ProfileUpdateForm, UserRegisterForm, UserUpdateForm




def index(request):
    return render(request, 'user/index.html')
def email(request):
    return render(request, "user/email.html")

########### register formu #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            bolum_name= form.cleaned_data.get('bolum_name')
            fakulte_name = form.cleaned_data.get('fakulte_name')
            ######################### mail ssistemi ####################################
            htmly = get_template('user/email.html')
            d = { 'username': username }
            d = { 'bolum_name': bolum_name }
            d = { 'fakulte_name': fakulte_name }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            #msg.send()
            #send_mail(subject, messages, from_email, to_list, fail_silently=Tre)
            ##################################################################
            messages.success(request, f'hesabınız olusturuldu ! giris yapabilirsiniz')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})
  
################ login formu ###################################################
def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            #login(request,user)
            messages.success(request, f' welcome {username} !!')
            return redirect('menu')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})   

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #f_form = FileUpdateForm(request.POST, request.FILES, instance=request.user.file)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #f_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile.html', context)

def logout(request):
	#logout(request)
	return redirect("menu")