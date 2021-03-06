# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class DetailListView(DetailView):
    model = Post
    template_name = 'detail.html'
