fruits = [
    {"name": "Apple", "calories": 130},
    {"name": "Avocado", "calories": 50},
    {"name": "Banana", "calories": 110},
    {"name": "Cantaloupe", "calories": 50},
    {"name": "Grapefruit", "calories": 60},
    {"name": "Grapes", "calories": 90},
    {"name": "Honeydew Melon", "calories": 50},
    {"name": "Kiwi", "calories": 40},
    {"name": "Lemon", "calories": 15},
    {"name": "Lime", "calories": 20},
    {"name": "Nectarine", "calories": 60},
    {"name": "Orange", "calories": 80},
    {"name": "Peach", "calories": 60},
    {"name": "Pear", "calories": 100},
    {"name": "Pineapple", "calories": 80},
    {"name": "Plums", "calories": 70},
    {"name": "Strawberries", "calories": 30},
    {"name": "Sweet Cherries", "calories": 100}
]
ans = input("Item: ").strip().title()
for fruit in fruits:
    if ans == fruit["name"]:
        print(f"Calories: {fruit['calories']}")
        break