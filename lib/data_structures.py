# Initial list of spicy foods
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

# 1. Get names of all spicy foods
def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

# 2. Get spiciest foods (heat level > 5)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

# 3. Print all spicy foods in the format "Name (Cuisine) | Heat Level: 🌶 * heat_level"
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_emoji = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")

# 4. Get a spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next(food for food in spicy_foods if food['cuisine'] == cuisine)

# 5. Print only the spiciest foods (heat level > 5)
def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

# 6. Get the average heat level of all spicy foods
def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat // len(spicy_foods)

# 7. Add a new spicy food to the list
def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods
