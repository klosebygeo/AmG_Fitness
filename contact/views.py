from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.
class ContactCreateView(CreateView):
    template_name = 'contact/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('/')