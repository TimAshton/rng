# Randomness of seed determines randomness of output.
#
# Same seed, same result.
#
# Process:
# * Obtain a seed integer.
# * Multiply it by itself.
#
# Inputs:
# * seed, cycles
#
# Limits
# * seed must be >= 11 in order to have a non-zero "middle".

# TODO:
# * Typing
# * Tests

import math
import argparse


def generate_segment(seed):
    # Double the seed.
    doubled_seed = seed ** 2

    # Create a str version of seed to find middle chars.
    doubled_seed_str = str(doubled_seed)

    #Store length of doubled seed.
    doubled_seed_length = len(doubled_seed_str)

    if doubled_seed_length % 2 == 0: # Use middle two digits as middle.
        mid_index = doubled_seed_length // 2 # Floor division.

        middle_int = int(doubled_seed_str[mid_index - 1 : mid_index + 1])
        random_number = middle_int ** 2

        return random_number
    else:
        middle_position = math.ceil(doubled_seed_length / 2)
        middle_index = middle_position - 1

        return doubled_seed_str[middle_index]


def generate_random_number(seed, cycles = 1):
    if cycles > 1:
        segments = ""

        i = 0
        while i < cycles:
            segments += str(generate_segment(seed))
            seed = generate_segment(seed)
            i += 1
  
        return segments
    else:
        a = generate_segment(seed)
        return a

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--seed", type=int, default=420, help="TODO")
    parser.add_argument("--cycles", type=int, default=1, help="TODO")

    args = parser.parse_args()

    print(generate_random_number(args.seed, args.cycles))
