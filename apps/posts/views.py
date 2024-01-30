from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from apps.posts.forms import PostForm
from apps.posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = "base/index.html"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    pk_url_kwarg = 'pk'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    success_url = '/'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.all()


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('homepage')

