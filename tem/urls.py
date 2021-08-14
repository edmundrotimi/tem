"""tem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#Admin settings
admin.site.site_header = 'Admin Area'
admin.site.site_title = 'Tem Admin'
admin.site.index_title= 'Tem Administration'
admin.empty_value_display= '**Empty**'

urlpatterns = [
    #admin document
    path(f'{settings.ADMIN_PATH}/doc/', include('django.contrib.admindocs.urls')),
    # admin path
    path(f'{settings.ADMIN_PATH}/', admin.site.urls),
    path(f'{settings.ADMIN_PATH}/doc/', include('django.contrib.admindocs.urls')),
    #honeypot
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    #pages urls
    path('', include('pages.urls')),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('blog/category/', include('categories.urls')),
    #ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
