#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Set result list
    result_list = []
    # Loop through recipe
    for ingredient in recipe:
        # Check if you have enough ingredients
        if ingredient not in ingredients or ingredients[ingredient] < recipe[ingredient]:
            return 0
        # If enough, divide and appen to list
        else:
            check_amount = ingredients[ingredient] // recipe[ingredient]
            result_list.append(check_amount)
    return min(result_list)


print(recipe_batches(
    {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
        'milk': 1288, 'flour': 9, 'sugar': 95}
))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
