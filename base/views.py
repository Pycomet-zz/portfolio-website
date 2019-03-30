from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact
from django.views.generic import TemplateView, CreateView
from .forms import HireForm

class Home(TemplateView):
    template_name = "base/home.html"

class About(TemplateView):
    template_name = "base/about.html"

class Contact(CreateView):
    """Contact Page"""

    model = Contact
    form_class = HireForm
    template_name = 'base/hire.html'

    def form_valid(self, form):
        hire = form.save()
        hire.save()
        messages.success(self.request, f'Your order has been sent! You would receive a reply shortly, thank you.')
        return redirect('home') 
    
class Portfolio(TemplateView):
    template_name = "base/portfolio.html"