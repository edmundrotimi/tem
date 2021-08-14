from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Blog


class HomepageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trendSession"] =  self.request.session.get('trend', 0)
        context["trending"] =  Blog.objects.filter(publish=True)[:4]
        context["allPost"] =  Blog.objects.filter(publish=True)
        context["posts"] =  Blog.objects.filter(publish=True)[:6]
        context["popular"] =  Blog.objects.filter(mark_as_popular=True, publish=True)[:6]
        context["purpose"] =  Blog.objects.filter(category__icontains='Purpose Discovery', publish=True)[:3]
        context["upliftment"] =  Blog.objects.filter(category__icontains='Spiritual Upliftment', publish=True)[:3]
        return context
    
