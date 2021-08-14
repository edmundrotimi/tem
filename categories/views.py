from django.shortcuts import render
from django.views.generic import View, ListView
from blog.models import Blog


class CategoriesDiscoveryView(ListView):
    model = Blog
    queryset = Blog.objects.filter(
        category__icontains='Purpose Discovery', publish=True)
    template_name = 'categories/discovery.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context


class CategoriesUpliftmentView(ListView):
    model = Blog
    queryset = Blog.objects.filter(
        category__icontains='Spiritual Upliftment', publish=True)
    template_name = 'categories/upliftment.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context


class CategoriesEmpowermentView(ListView):
    model = Blog
    queryset = Blog.objects.filter(
        category__icontains='Youth Empowerment', publish=True)
    template_name = 'categories/empowerment.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context


class CategoriesFoundationView(ListView):
    model = Blog
    queryset = Blog.objects.filter(
        category__icontains='TM Foundation', publish=True)
    template_name = 'categories/foundation.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context


class CategoriesTrainingView(ListView):
    model = Blog
    queryset = Blog.objects.filter(
        category__icontains='Training School', publish=True)
    template_name = 'categories/training.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context
