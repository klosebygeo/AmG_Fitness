from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class GalleryTemplateView(TemplateView):
    template_name = 'gallery/gallery.html'