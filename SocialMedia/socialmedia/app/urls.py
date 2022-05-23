from django.urls import path
from .import views
from .views import *
from .forms import *
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('',views.home,name='home'),
  path('story/',views.StoryForm,name="story"),
]