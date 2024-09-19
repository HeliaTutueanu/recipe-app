from django.urls import path
from .views import home
from .views import RecipesListView, RecipesDetailView, RecipesAuthorView, create_recipe, update_recipe, delete_recipe, about
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

app_name = 'recipes'  

urlpatterns = [
   path('', home, name='home'),
   path('aboutme/', about, name='about'),
   path('recipes/', RecipesListView.as_view(), name='recipes'),
   path('recipes/<int:pk>', RecipesDetailView.as_view(), name='detail'),
   path("create/", create_recipe, name="create_recipe"),
   path("update/<int:pk>/", update_recipe, name="update_recipe"),
   path("delete/<int:pk>/", delete_recipe, name="delete_recipe"),
   re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]