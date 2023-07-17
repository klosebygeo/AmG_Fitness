from django.urls import path

from home import views

urlpatterns = [
    path('homepage',views.HomeTemplateView.as_view(), name='homepage')
]
