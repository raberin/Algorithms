#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# Naive Recursive Implementation O(3^n)
def eating_cookies_naive(n, cache=None):
    # Base cases
    if n < 3:
        return n
    elif n == 3:
        return 4
    # Recurse through all possible permutations
    return eating_cookies_naive(n-1) + eating_cookies_naive(n-2) + eating_cookies_naive(n-3)


# print(eating_cookies_naive(30))


# Memoized/Cached Recursive Implementation O(n^2)
def eating_cookies(n, cache={0: 1, 1: 1, 2: 2, 3: 4}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(
            n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return cache[n]


print(eating_cookies(5))


# Iterative Bottom-Down Approach O(n) -- Needs work/refinement
def eating_cookies_iterative(n):
    # Base Case
    if n <= 2:
        return n
    elif n == 3:
        return 4
    # Set cookie conditions for n == 3
    #
    one_cookie = 4
    two_cookie = 2
    three_cookie = 1

    for i in range(3, n):
        current = one_cookie + two_cookie + three_cookie
        three_cookie = two_cookie
        two_cookie = one_cookie
        one_cookie = current

    return current


print(eating_cookies_iterative(5))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
