#!/usr/bin/python

import argparse


# Naive O(n^2)
def find_max_profit_naive(prices):
    # Make current_buy_price and max_profit_so_far
    max_profit_so_far = prices[1] - prices[0]
    # Double Loop comparing the potential_profit vs max_profit_so_far
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            # Calculate difference of buy price with sell price
            potential_profit = prices[j] - prices[i]
            # Set value if found higher profit price
            if max_profit_so_far < potential_profit:
                max_profit_so_far = potential_profit
    return max_profit_so_far

# Optimized O(n)


def find_max_profit(prices):
    # Set max_profit_so_far
    max_profit_so_far = prices[1] - prices[0]
    # Loop through, looking for smallest number from 1 to end indices
    for i in range(len(prices) - 1):
        # Set current_buy_price and find max_selling_price
        current_buy_price = prices[i]
        max_selling_price = max(prices[i + 1:])
        # Calculate difference of buy and sell
        potential_profit = max_selling_price - current_buy_price
        # Set value if found higher profit price
        if potential_profit > max_profit_so_far:
            max_profit_so_far = potential_profit
    return max_profit_so_far


print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
