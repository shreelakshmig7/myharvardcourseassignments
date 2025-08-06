def get_input():
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height < 9:
                break
        except ValueError:
            print("Enter valid number in the range of 0-8")
    return height


def build_tree(height):
    for i in range(height):
        print(" " * (height - (i + 1)), end="")
        print("#" * (i+1), end="")
        print(" " * 2, end="")
        print("#" * (i + 1))


def main():
    height = get_input()
    build_tree(height)


if __name__ == "__main__":
    main()
