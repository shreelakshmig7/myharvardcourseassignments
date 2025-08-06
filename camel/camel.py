def covert_snake_case(camelCase):
    if camelCase.islower():
        return camelCase

    snake_case_str = camelCase
    for letter in camelCase:
        if letter.isupper():
           new_sub_str = "_"+letter.lower()
           snake_case_str = snake_case_str.replace(letter, new_sub_str)

    return snake_case_str


def main():
    inptStr = input("camelCase: ")
    outpt_str = covert_snake_case(inptStr)
    print(f"snake_case: {outpt_str}")


if __name__ == "__main__":
    main()
