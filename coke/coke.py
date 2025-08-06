def validate_input(input_data):
    if input_data == 25 or input_data == 10 or input_data == 5:
        return True
    else:
        return False


def main():
    price = 50
    total = 0
    while total < price:
        print(f"Amount Due: {price-total}")
        inpt_amt = int(input("Insert Coin: "))
        if validate_input(inpt_amt):
            total = total + inpt_amt

    print(f"Change Owed: {total-price}")



if __name__ == "__main__":
    main()
