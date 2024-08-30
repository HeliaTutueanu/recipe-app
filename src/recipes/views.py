from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, 'recipes/home.html')

@login_required
def records(request):
   return render(request, 'recipes/records.html')

class RecipeListView(LoginRequiredMixin, ListView):
   model = Recipe
   template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'