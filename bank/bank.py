def howMuch2Pay(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


def main():
    greetMsg = input("Greeting: ").strip().lower()
    payment = howMuch2Pay(greetMsg)
    print(payment)


main()
