from django.db import models
from django.utils import timezone
from users.models import User

class Recipe(models.Model):
    name =  models.CharField(max_length=100)
    cooking_time = models.IntegerField(help_text='in min', default=0)
    ingredients = models.CharField(max_length=250, help_text="Each ingredient seperated by a comma, like 'Eggs, Butter'")
    pic = models.ImageField(upload_to='recipes', help_text="Choose an image with minimum 250px width.", default='no_picture.jpg')
    instructions = models.TextField(help_text="No instructions...", null=True, blank=True)
    _difficulty = models.CharField(max_length=120, default='')
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.difficulty} - {self.cooking_time}"
    
    @property
    def difficulty(self):
        if self._difficulty == '':
            self.calc_difficilty()
        return self._difficulty
    
    def calc_difficilty(self):
        ingredients_len = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and ingredients_len < 4:
            self._difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            self._difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            self._difficulty = "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len >= 4:
            self._difficulty = "Hard"
            