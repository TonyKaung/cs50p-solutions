import random

def main():
    level = get_level()
    score = 0

    # run 10 problems
    for _ in range(10):
        count = 0
        x = generate_integer(level)
        y = generate_integer(level)

        # ask the same problem until the user gets it right or has tried 3 times
        while count < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    count += 1
                    # if the user has tried 3 times, show the correct answer
                    if count == 3:
                        print(f"{x} + {y} = {x + y}")
            except ValueError:
                print("EEE")
                count += 1
                # if the user has tried 3 times, show the correct answer
                if count == 3:
                    print(f"{x} + {y} = {x + y}")

    # print the final score
    print(f"Score: {score}")

def get_level():
    # try until the user inputs a valid level
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    return random.randint(0, 10 * level)

if __name__ == "__main__":
    main()