from django.urls import path
from .views import profile, signup_view
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

app_name = 'users'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
