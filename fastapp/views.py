from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView

# Create your views here.
class FastAppView(TemplateView):
    template_name = 'fastapp/fastapp.html'