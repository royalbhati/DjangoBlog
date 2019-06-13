from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.apps import apps

Post=apps.get_model('blog','Post')
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        form=UserRegisterForm()

    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    u_form=UserUpdateForm(request.POST,instance=request.user)
    p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request,f'profile updated for {username}')
        return redirect('profile')
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
def saved_posts(request):
    Query_Set=Post.objects.filter(saved=request.POST.get('profile'))
    print("************************",Query_Set)
    context={
        'posts':Query_Set
    }
    return render(request,'users/saved.html',context)    