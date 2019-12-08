from calendar import monthrange
from datetime import datetime, date

from django.contrib.admin import ModelAdmin
from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView

from fieldsapp.admin import download_csv
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm



class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.exclude(status=False)


class ReservedDetailView(DetailView):
    model = Post
    template_name = 'post_reserved.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')





