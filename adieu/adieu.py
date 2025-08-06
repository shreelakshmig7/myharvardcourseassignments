import inflect

def print_output(names, prefix_str):
    p = inflect.engine()
    print(prefix_str + " " + p.join(names))


def main():
    nameList = []
    prefix_str = "Adieu, adieu, to"
    while True:
        try:
            nameList.append(input("Name: "))
        except EOFError:
            break;

    if len(nameList) != 0:
        print_output(nameList, prefix_str)


if __name__ == "__main__":
    main()
