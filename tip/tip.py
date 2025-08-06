def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    value = d.removeprefix("$")
    return float(value)


def percent_to_float(p):
    value = p.removesuffix("%")
    percVal = round(float(value)/100, 2)
    return percVal


main()
