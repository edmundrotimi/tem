import uuid
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from .validateimage import clean_image
from .chioces import categories


class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title', unique_with='id')
    intro_text = models.TextField(max_length=150)
    category = models.CharField(max_length=50,
                                choices=categories, default='Purpose Discovery')
    details = RichTextUploadingField(max_length=2000)
    featured_img = models.ImageField(upload_to='img/blog/featured',
                                     validators=[
                                         clean_image], verbose_name='Featured Image',
                                     help_text='Upload of post featured image')
    gallery_image_1 = models.ImageField(upload_to='img/blog/featured',
                                        validators=[
                                            clean_image], help_text='add optional images to post')
    gallery_image_2 = models.ImageField(upload_to='img/blog/featured',
                                        validators=[
                                            clean_image], help_text='add optional images to post')
    gallery_image_3 = models.ImageField(upload_to='img/blog/featured',
                                        validators=[
                                            clean_image], help_text='add optional images to post')
    gallery_image_4 = models.ImageField(upload_to='img/blog/featured',
                                        validators=[
                                            clean_image], help_text='add optional images to post')
    gallery_image_5 = models.ImageField(upload_to='img/blog/featured',
                                        validators=[
                                            clean_image], help_text='add optional images to post')
    gallery_image_6 = models.ImageField(upload_to='img/blog/featured',
                                        validators=[
                                            clean_image], help_text='add optional images to post')
    mark_as_popular = models.BooleanField(
        default=True, verbose_name='Mark As Popular', help_text='mark post as popular')
    publish = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['last_updated']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
