from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.

class SnackList(ListView):
    template_name = 'snacklist.html'
    model = Snack


class SnackDetail(DetailView):
    template_name = 'snackdetail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snackcreate.html'
    model = Snack
    fields = ['title','purchaser','description']


class SnackUpdateView(UpdateView):
    template_name = 'snackupdate.html'
    model = Snack
    fields = ['title','purchaser','description']


class SnackDeleteView(DeleteView):
    template_name = 'snackdelete.html'
    model = Snack
    success_url = reverse_lazy('snacklist')
