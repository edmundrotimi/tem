from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, SearchView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog'),
    path('search', SearchView.as_view(), name='blogSearch')
]
