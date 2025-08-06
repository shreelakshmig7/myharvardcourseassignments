def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(numPlate):
    if len(numPlate) < 2 or len(numPlate) > 6:
        return False
    elif not numPlate.isalnum():
        return False
    elif not numPlate[0:2].isalpha():
        return False
    elif numPlate.isalpha():
        return True
    else:
        for s in numPlate[2:]:
            if s.isdigit():
                if s == '0':
                    return False
                sIndex = numPlate.find(s)
                if numPlate[sIndex:].isdigit():
                    return True
                else:
                    return False


main()
