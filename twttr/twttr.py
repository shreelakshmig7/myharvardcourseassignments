def remove_vowels(input_data):
    output_data = ""
    for letter in input_data:
        if letter not in "aeiouAEIOU":
           output_data = output_data + letter

    return output_data


def main():
    inpt_str = input("Input: ")
    outpt_str = remove_vowels(inpt_str)
    print(f"Output: {outpt_str}")


if __name__ == "__main__":
    main()
