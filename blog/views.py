from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.contrib.auth.models import User 

def home(request):
    context ={
        'posts':Post.objects.all(),
        'title':"context"
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html')

# def counter(request):
#     if(request.GET.get('hcount'))
def like_post(request):
    # print()
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.hearts.add(request.user)
    post.save()
    return redirect('blog-home')
def save_post(request):
    postq=Post.objects.filter(id=request.POST.get('post_id'))
    post=get_object_or_404(postq)
    query_set=User.objects.filter(username=request.user)
    user=get_object_or_404(query_set)
    user.profile.saved.add(post)
    user.profile.save()
    return redirect('blog-home')