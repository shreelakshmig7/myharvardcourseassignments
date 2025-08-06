import emoji

def main():
    input_emoji = input("Input: ")
    print("Output: ", emoji.emojize(input_emoji, language='alias'))


if __name__ == "__main__":
    main()
