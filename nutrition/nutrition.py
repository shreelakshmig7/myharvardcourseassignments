def get_calories(fruit):
    fruit_calories = {"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60,
                      "Grapes": 90, "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15, "Lime": 20,
                      "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100, "Pineapple": 50, "Plums": 70,
                      "Strawberries": 50, "Sweet Cherries": 100, "Tangerine": 50, "Watermelon": 80}
    if fruit in fruit_calories:
        return fruit_calories[fruit]
    else:
        return None


def main():
    item = input("Item: ").title()
    calories = get_calories(item)
    if calories:
        print(f"Calories: {calories}")


main()
