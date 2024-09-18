from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import pandas as pd
from .forms import RecipesSearchForm, CreateRecipeForm
from .utils import get_recipename_from_id, get_chart
from django.db.models import Q
from users.models import User
from django.core.paginator import Paginator, EmptyPage


def home(request):
   return render(request, 'recipes/recipes_home.html')

def about(request):
   return render(request, 'recipes/about_me.html')

class RecipesListView(ListView):
   model = Recipe
   
   def get(self, request):
      form = RecipesSearchForm()
      recipes = Recipe.objects.all()
      paginator = Paginator(recipes, 9)
      page_number = request.GET.get('page', 1)
      try:
         recipes = paginator.page(page_number)
      except EmptyPage:
         recipes = paginator.page(paginator.num_pages)
      return render(request, 'recipes/recipes_list.html', {'form': form, 'recipes': recipes, 'page_obj': recipes})
   
   def post(self, request):
      form = RecipesSearchForm(request.POST)
      recipes = Recipe.objects.all()
      chart = None

      if form.is_valid():
         recipe_name = form.cleaned_data.get('recipe_name')
         chart_type = form.cleaned_data.get('chart_type')

         qs = Recipe.objects.filter(Q(name__icontains=recipe_name) | Q(ingredients__icontains=recipe_name))
         if qs.exists():
            recipes = pd.DataFrame(qs.values())
            recipes['difficulty'] = recipes.apply(lambda row: get_recipename_from_id(row['id']).difficulty, axis=1)
         
            chart = get_chart(chart_type, recipes, labels=recipes['id'].values)
         else:
            recipes = pd.DataFrame()

      context = {
         'form': form,
         'recipes': recipes,
         'chart': chart,
      }
      return render(request, 'recipes/recipes_list.html', context)
   

class RecipesDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/recipes_details.html'

class RecipesAuthorView(LoginRequiredMixin, DetailView):
   model = User
   template_name = 'recipes/recipes_author.html'

   def get_queryset(self):
      return User.objects.filter(pk=self.kwargs['pk'])

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['recipes'] = Recipe.objects.filter(author=self.object)
      return context

@login_required
def create_recipe(request):
   if request.method == 'POST':
      form = CreateRecipeForm(request.POST, request.FILES)
      if form.is_valid():
         recipe = form.save(commit=False)
         recipe.author = request.user

         recipe.save()
      else:
         print('Something went wrong.')

   return redirect('recipes:recipes')

@login_required
def update_recipe(request, pk):
   recipe = get_object_or_404(Recipe, pk=pk)
   if request.method == 'POST':
      form = CreateRecipeForm(request.POST, request.FILES, instance=recipe)
      if form.is_valid():
         recipe.save()
         return redirect('recipes:detail', pk=recipe.pk)
      else:
         form = CreateRecipeForm(instance=recipe)
         print('Something went wrong.')

   return render(request, 'recipes/recipes_details.html', {'object': recipe})

@login_required
def delete_recipe(request, pk):
   recipe = get_object_or_404(Recipe, pk=pk)
   recipe.delete()
   return redirect('recipes:recipes')