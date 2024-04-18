from django.urls import path
from .views import (RecipeStepApiView)

urlpatterns = [
  path('recipe-steps', RecipeStepApiView.as_view())
]