def main():
    inputTime = input("What time is it? ")
    noOfHours = convert(inputTime)
    if noOfHours >= 7.0 and noOfHours <= 8.0:
        print("breakfast time")
    elif noOfHours >= 12.0 and noOfHours <= 13.0:
        print("lunch time")
    elif noOfHours >= 18.0 and noOfHours <= 19.0:
        print("dinner time")
    else:
        return


def convert(time):
    if ("a.m." in time) or ("p.m." in time):
        actualtime, dayNight = time.split(" ")
        hours, minutes = actualtime.split(":")
        if dayNight == "p.m." and int(hours) < 12:
            hours = int(hours) + 12
    else:
        hours, minutes = time.split(":")

    minToFlt = float(minutes) / 60
    fltNumTime = float(hours) + round(minToFlt, 2)
    return fltNumTime


if __name__ == "__main__":
    main()
