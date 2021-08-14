from django.contrib import admin, messages
from .models import Blog
from reversion.admin import VersionAdmin

# custome admin action


def unpublish_post(modeladmin, request, queryset):
    if queryset.filter(publish=True):
        queryset.update(publish=False)
    else:
        queryset.update(publish=True)
    messages.add_message(request, messages.SUCCESS,
                         'Selected post published/unpublished successfully.')


unpublish_post.short_description = 'Publish/Unpublish Post'


class AdminBlog(VersionAdmin, admin.ModelAdmin):
    list_display = ['title', 'category',
                    'last_updated', 'mark_as_popular', 'publish']
    list_display_links = ['title', 'category', 'last_updated']
    list_filter = ['publish', ]
    date_hierarchy = 'last_updated'
    list_per_page = 50
    view_on_site = True
    actions = [unpublish_post]
    actions_on_top = True
    actions_on_bottom = True
    view_on_site = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['title', 'intro_text', 'details',
                     'category', 'featured_img', 'last_updated', 'publish']
    fieldsets = [
        ['Post Info', {
            'fields': ['title', 'intro_text', 'category']
        }],
        ['Post Details', {
            'classes': ['collapse'],
            'fields': ['details', 'mark_as_popular']
        }],
        ['Media', {
            'classes': ['collapse'],
            'fields': ['featured_img', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4',
                       'gallery_image_5', 'gallery_image_6']
        }],
        ['Timeline', {
            'classes': ['collapse'],
            'fields': ['publish', 'last_updated']
        }],
    ]


admin.site.register(Blog, AdminBlog)
