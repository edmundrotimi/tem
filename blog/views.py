import json
from django.shortcuts import render
from django.contrib import messages
from django.core.management import call_command
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import View, TemplateView, ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.filter(publish=True)
    context_object_name = 'posts'
    template_name = 'blog/posts.html'
    paginate_by = 4


class BlogDetailView(DetailView):
    model = Blog
    queryset = Blog.objects.filter(publish=True)
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        #set session
        trendList = self.request.session.get('trend', 0)
        querysetSlug = self.request.path.split('/')[len(self.request.path.split('/'))-2]
        getQuerysetInstance = Blog.objects.get(slug=querysetSlug)
        getQuerysetId = str(getQuerysetInstance.id)

        #check if session exist
        if trendList != 0 and trendList != None:
            for i in trendList:
                if getQuerysetId not in i:
                    self.request.session['trend'] = trendList.append(
                        getQuerysetId)
        else:
            self.request.session['trend'] = [getQuerysetId]

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context


class SearchView(ListView):
    model = Blog
    queryset = Blog.objects.filter(publish=True)
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        if self.request.method == 'GET':
            searchQuery = self.request.GET.get('search')
            queryset = Blog.objects.filter(publish=True)
            if searchQuery:
                queryset = Blog.objects.filter(
                    Q(title__icontains=searchQuery) |
                    Q(intro_text__icontains=searchQuery) |
                    Q(details__icontains=searchQuery) |
                    Q(category__icontains=searchQuery) |
                    Q(last_updated__icontains=searchQuery)
                )
                return queryset
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allPost"] = Blog.objects.filter(publish=True)
        return context
