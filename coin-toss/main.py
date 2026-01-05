import random

def flip_coin():
    if random.randint(1,2) == 1:
        return "H"
    else:
        return "T"


def main(tries, match_target):
    consecutive_matches = 0
    last_result = ""
    flips = 0

    while(flips < tries):
        flips += 1
        rez = flip_coin()

        if rez == last_result:
            consecutive_matches += 1
        else:
            consecutive_matches = 0

        print(flips, rez, consecutive_matches)

        if consecutive_matches == match_target - 1:
            print(f"!!! {match_target} Consecutive Tosses !!!")

            break

        last_result = rez

if __name__ == "__main__":
    main(tries = 10000, match_target = 10)