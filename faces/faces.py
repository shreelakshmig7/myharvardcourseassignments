def convert(txt):
    newTxt = txt.replace(":)", "🙂")
    newTxt = newTxt.replace(":(", "🙁")
    return newTxt


def main():
    inputStr = input()
    retTxt = convert(inputStr)
    print(retTxt)


main()
