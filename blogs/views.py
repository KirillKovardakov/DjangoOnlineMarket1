from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Blog


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.count_views += 1
        obj.save(update_fields=["count_views"])
        return obj


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"

    # фильтрация опубликованных
    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ["headline", "content", "preview", "is_published"]
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blogs:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["headline", "content", "preview", "is_published"]
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy('blogs:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blogs:blog_list")
