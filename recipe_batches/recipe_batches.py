#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_ratio = math.inf

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0
    ratio = math.floor(ingredients[ingredient] / amount)
    if ratio < min_ratio:
      min_ratio = ratio
    
  return min_ratio


if __name__ == '__main__':
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print(recipe_batches(recipe, ingredients))