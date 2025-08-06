import random


def main():
    level = get_level()
    correct_ans = 0
    for _ in range(10):
        nums = generate_integer(level)
        correct_ans = correct_ans + check_for_ans(nums, sum(nums))

    print(f"Score: {correct_ans}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not  in (1, 2, 3):
                continue
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    start = 0
    up_to = 0
    match level:
        case 1:
            start = 0
            up_to = 10
        case 2:
            start = 10
            up_to = 100
        case 3:
            start = 100
            up_to = 1000

    return [random.randint(start, up_to), random.randint(start, up_to)]


def check_for_ans(two_nums, sum):
    tries = 3
    ans = -1
    while ans != sum and tries > 0:
        try:
            ans = int(input(str(two_nums[0]) + " + "  + str(two_nums[1]) + " = "))
            if ans != sum:
                tries = tries - 1
                print("EEE")
        except ValueError:
            print("EEE")
            tries = tries - 1

    if tries == 0:
        print(f"{two_nums[0]} + {two_nums[1]} = {sum}")
        return 0
    elif tries == 3:
        return 1



if __name__ == "__main__":
    main()
