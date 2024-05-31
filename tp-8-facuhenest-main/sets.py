from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    new_set = set(dish_ingredients)
    return dish_name,new_set

def check_drinks(drink_name, drink_ingredients):
    empty_set = set() 
    set_ingredients = set(drink_ingredients)   
    if set_ingredients.intersection(ALCOHOLS) == empty_set:
        return f"{drink_name} Mocktail"
    else:
        return f"{drink_name} Cocktail"
