spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_spicy = []
    for food in spicy_foods:
        new_spicy.append(food["name"])
    return new_spicy

def get_spiciest_foods(spicy_foods):
    new_level = []
    for level in spicy_foods:
        if level["heat_level"] >= 5:
            new_level.append(level)
    return new_level

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        if food["heat_level"] >= 5:
            print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

def get_average_heat_level(spicy_foods):
    total = 0
    count = 0
    for food in spicy_foods:
        total += food["heat_level"]
        count += 1
        average = total/count
    return average

def create_spicy_food(spicy_foods, spicy_food):
    new_list = spicy_foods
    new_list.append(spicy_food)
    return new_list
