import re


def get_card_number():
    while True:
        card_number = input("Number: ")
        if card_number.isdigit():
            break
    return card_number


def find_checksum(card_number):
    reverse_list = card_number[::-1]
    even_place_num = [2 * int(i) for i in reverse_list[1::2]]
    odd_place_num = [int(i) for i in reverse_list[0::2]]
    sum_even_num = 0

    for num in even_place_num:
        if num > 9:
            sum_even_num += sum([int(i) for i in str(num)])
        else:
            sum_even_num += num

    final_sum = sum_even_num + sum(odd_place_num)
    return final_sum


def validate_card(card_number):
    type_of_card = ""

    if re.match("^3[4|7][0-9]{13}$", card_number):
        type_of_card = "AMEX"
    elif re.match("^5[1-5][0-9]{14}$", card_number):
        type_of_card = "MASTERCARD"
    elif re.match("^4[0-9]{12}([0-9]{3})?$", card_number):
        type_of_card = "VISA"
    else:
        print("INVALID")

    if type_of_card != "":
        checksum = find_checksum(card_number)
        if checksum % 10 == 0:
            print(f"{type_of_card}")
        else:
            print("INVALID")


def main():
    card_number = get_card_number()
    validate_card(card_number)


if __name__ == "__main__":
    main()
