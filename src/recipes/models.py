from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name= models.CharField(max_length=120)

    cooking_time = models.IntegerField(help_text='in min', default=0)
    ingredients = models.CharField(max_length=250, null=True,
    help_text="Each ingredient seperated by a comma'")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} - {self.ingredients} - {self.cooking_time}"