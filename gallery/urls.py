from django.urls import path

from gallery import views

urlpatterns = [
     path('gallery', views.GalleryTemplateView.as_view(), name='gallery')
]