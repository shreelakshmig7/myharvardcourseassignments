def find_total(food, price):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    price = price + menu[food]
    print(f'Total: ${price:.2f}')
    return price


def main():
    total = 0
    while True:
        try:
            item = input("Item: ")
            total = find_total(item.title(), total)
        except EOFError:
            print()
            break
        except KeyError:
            pass



main()
