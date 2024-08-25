from django.db import models

class Recipe(models.Model):
    name= models.CharField(max_length=120)

    cooking_time = models.IntegerField(help_text='in min', default=0)
    ingredients = models.CharField(max_length=250, null=True,
    help_text="Each ingredient seperated by a comma'")

    def __str__(self):
        return f"{self.name} - {self.ingredients} - {self.cooking_time}"