import random


def guess_num(n):
    rand_num = random.randint(0, n)
    while True:
        try:
            ans = int(input("Guess: "))
            if ans == rand_num:
                print("Just right!")
                break
            elif ans > rand_num:
                print("Too large!")
                continue
            elif ans < rand_num:
                print("Too small!")
                continue
        except TypeError:
            pass
        except ValueError:
            pass


def main():
    n = 0
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except TypeError:
            pass
        except ValueError:
            pass

    guess_num(n)


if __name__ == "__main__":
    main()
