import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry_django import mutations

from .types import RecipeStep, RecipeStepInput

@strawberry.type
class Query:
    recipe_steps: list[RecipeStep] = strawberry_django.field()

@strawberry.type
class Mutation:
    add_recipe_step : RecipeStep = mutations.create(RecipeStepInput)

schema = strawberry.Schema(
    query=Query, 
    mutation=Mutation, 
    extensions=[DjangoOptimizerExtension()])