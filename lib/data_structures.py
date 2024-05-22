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
    return [i["name"] for i in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [i for i in spicy_foods if i["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        heat_level = "🌶" *i["heat_level"]
        cuisine = i["cuisine"]
        print(f'{i["name"]} ({cuisine}) | Heat Level: {heat_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        if i["cuisine"] == cuisine:
            return i

def print_spiciest_foods(spicy_foods):
    above_5 = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(above_5)


def get_average_heat_level(spicy_foods):
    total_heat = sum([i["heat_level"] for i in spicy_foods])
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods,{
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }))
