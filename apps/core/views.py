from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Client
from .forms import ClientForm




class ClientMixin(object):
    model = Client


class CreatView(ClientMixin, CreateView):
    form_class = ClientForm
    template_name = 'core/create_client.html'


class ListView(ClientMixin, ListView):
    template_name = 'core/index.html'
    context_object_name = 'clients'
    paginate_by = 4


class UpdateView(ClientMixin, UpdateView):
    template_name = 'core/client_update.html'
    is_update_view = True
    form_class = ClientForm


class DeleteView(ClientMixin, DeleteView):
    success_url = reverse_lazy('core:home_view')
  

class DetailView(ClientMixin, DetailView):
    template_name = 'core/client_detail.html'