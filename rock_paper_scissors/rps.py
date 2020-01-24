#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Create combinations and options arr
    combinations = []
    options = ['rock', 'paper', 'scissors']

    # Inner helper recursion function
    def get_results(rounds, result=[]):
        # Base Case - Append result arr to combinations arr
        if rounds == 0:
            return combinations.append(result)
        else:
            # Loop through options arr recursively adding each option into results arr
            for i in options:
                get_results(rounds - 1, result + [i])
    # Call helper function
    get_results(n, [])
    # Return combination
    return combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
