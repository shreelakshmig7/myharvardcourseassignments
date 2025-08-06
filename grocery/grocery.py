def get_input():
    glist = dict()
    while True:
        try:
            item = input().upper()
            if item in glist:
                glist[item] += 1
            else:
                glist.update({item:1})
        except EOFError:
            print()
            break
        except KeyError:
            pass

    return glist


def main():
    grocery_list = get_input()
    for items in sorted(grocery_list):
        print(f"{grocery_list[items]} {items}")


main()
