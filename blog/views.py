from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/posts/'  # перенаправление после успешного создания


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/update_form.html'
    success_url = '/posts/'


def delete_post(request, id):
    item = Post.objects.get(id=id)
    item.delete()
    return redirect('/posts/')

