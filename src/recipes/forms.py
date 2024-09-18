from django import forms
from django.forms import TextInput, Textarea, NumberInput
from .models import Recipe

CHART__CHOICES = (
   ('bar_chart', 'Bar chart'),
   ('pie_chart', 'Pie chart'),
   ('line_chart', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [ "name", "cooking_time", "ingredients", "instructions", "pic"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'cooking_time': NumberInput(attrs={'class': 'form-control'}),
            'ingredients': TextInput(attrs={'class': 'form-control'}),
            'instructions': Textarea(attrs={'class': 'form-control'}),
        }