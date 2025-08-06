import sys

def main():
    if len(sys.argv) >2 and not (sys.argv[1].endswith(".py")):
        sys.exit()

    no_of_code_lines = 0

    try:
        with open(sys.argv[1]) as fp:
            for eachLine in fp:
                eachLine.lstrip()
                if not (eachLine.startswith("#") and eachLine:
                    continue


if "__name__" == "__main__":
    main()
