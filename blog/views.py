from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost


class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'body', 'preview']
    success_url = reverse_lazy('blog:view_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class PostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'body', 'preview']

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view_post', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:view_list')
