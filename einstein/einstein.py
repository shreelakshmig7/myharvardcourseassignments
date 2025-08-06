def findEnergy(mass):
    energy = mass * (300000000 ** 2)
    return energy


def main():
    m = int(input("m: "))
    energy = findEnergy(m)
    print(f"E: {energy}")


main()
