def convert(fraction):
    try:
        vals = fraction.split("/")
        val1 = int(vals[0])
        val2 = int(vals[1])
        if val2 == 0:
            raise ZeroDivisionError
        if val1 > val2:
            raise ValueError

        perc = round((val1 / val2) * 100)
        return perc

    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
            return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f'{percentage}%')


def main():
    fracInpt = input("Fraction: ")
    perc = convert(fracInpt)
    print(gauge(perc))


if "__name__" == "__main__":
    main()
