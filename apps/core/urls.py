# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import ListView, DetailView, DeleteView, UpdateView, CreatView


urlpatterns = [
    url(r'^$', ListView.as_view(), name='home_view'),
    url(r'^client/edit/(?P<pk>\d+)/$', UpdateView.as_view(), name='edit_view'),
    url(r'^client/detail/(?P<pk>\d+)/$', DetailView.as_view(), name='detail_view'),
    url(r'^client/delete/(?P<pk>\d+)/$', DeleteView.as_view(), name='delete_view'),
    url(r'^client/create/$', CreatView.as_view(), name='create_view'),
    ]