from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import BlogPost


class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'body']
    success_url = reverse_lazy('blog:view_list')


class PostListView(ListView):
    model = BlogPost


class PostDetailView(DetailView):
    model = BlogPost


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'body']
    success_url = reverse_lazy('blog:view_list')


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:view_list')
