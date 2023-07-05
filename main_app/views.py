from django.shortcuts import render
from .models import Make
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DeleteView
from django.urls import reverse

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class MakeCreate(CreateView):
    model = Make
    fields = ['name', 'image', 'country']
    template_name = "make_create.html"
    success_url = '/makes/'

class MakeList(TemplateView):
    template_name = "make_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["makes"] = Make.objects.filter(name__icontains=name)
        else:
            context["makes"] = Make.objects.all()
        return context

class MakeDetail(DeleteView):
    model = Make
    template_name = "make_detail.html"


class MakeUpdate(UpdateView):
    model = Make
    fields = ['name', 'image', 'country']
    template_name = "make_update.html"
    success_url = "/makes/"

    def get_success_url(self):
        return reverse('make_detail', kwargs={'pk': self.object.pk})

class MakeDelete(DeleteView):
    model = Make
    template_name = "make_delete_confirmation.html"
    success_url = "/makes/"
