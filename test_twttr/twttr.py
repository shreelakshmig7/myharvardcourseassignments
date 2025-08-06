def main():
    inpt = input("Please enter a word: ")
    print("Output: ", shorten(inpt))


def shorten(word):
    new_word = word
    for i in ["a", "e", "i", "o", "u"]:
        if i in word.lower():
            new_word = new_word.replace(i, "")
            new_word = new_word.replace(i.upper(), "")

    return new_word


if __name__ == "__main__":
    main()
