def calculate_percentage(x, y):
    perc = round((x / y) * 100)
    if perc == 1 or perc < 1:
        print("E")
    elif perc == 99 or perc > 99:
        print("F")
    else:
        print(f'{perc}%')


def main():
    while True:
        try:
            fracInpt = input("Fraction: ")
            vals = fracInpt.split("/")
            val1 = int(vals[0])
            val2 = int(vals[1])
            if val1 > val2:
                continue
            calculate_percentage(val1, val2)
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


main()
