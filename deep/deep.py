def main():
    ansStr = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if ansStr == "42" or ansStr == "forty two" or ansStr == "forty-two":
        print("Yes")
    else:
        print("No")


main()
