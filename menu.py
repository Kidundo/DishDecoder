﻿# Define a dictionary with menu items and their ingredients
menu_items = {
    "Spaghetti Bolognese": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "olive oil", "salt", "pepper"],
    "Caesar Salad": ["romaine lettuce", "croutons", "parmesan cheese", "Caesar dressing", "chicken breast", "salt", "pepper"],
    "Margherita Pizza": ["pizza dough", "tomato sauce", "mozzarella cheese", "basil", "olive oil", "salt"],
    "Chicken Curry": ["chicken breast", "curry powder", "coconut milk", "onion", "garlic", "ginger", "salt", "pepper"]
}

# Function to get ingredients for a given menu item
def get_ingredients(menu_item):
    return menu_items.get(menu_item.strip(), [])

# Main program: Accept multiple menu items and print unique ingredients
user_input = input("Enter menu items separated by commas (e.g., Spaghetti Bolognese, Caesar Salad): ")
menu_list = user_input.split(",")

# Collect all ingredients
all_ingredients = []
for item in menu_list:
    ingredients = get_ingredients(item)
    if ingredients:
        all_ingredients.extend(ingredients)
    else:
        print(f"Warning: '{item.strip()}' not found in menu database.")

# Create a set to get unique ingredients
unique_ingredients = sorted(set(all_ingredients))

# Display the result
print("\nUnique Ingredients:")
for ingredient in unique_ingredients:
    print(f"- {ingredient}")
    
