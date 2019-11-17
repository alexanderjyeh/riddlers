#!/usr/bin/env python3

import random
import statistics

def dice(n):
    """Rolls a n-sided dice, will return an int from [0,n-1]"""
    if n < 2:
        raise ValueError("The dice must have more than 1 side", n)

    return random.randrange(0,n-1)

def game(n = 10):
    """Will play the game laid out in The Riddler Nov. 15, 2019.
    n is the size of the dice, defaults to 10."""
    
    rolls = "0.{}".format(dice(n))

    while int(rolls[-1]) > 0:
        val = dice(n)
        if val < int(rolls[-1]):
            rolls += str(val)

    return float(rolls)


def some_games(many):
    """Will play the game many times"""
    total = []
    for i in range(many):
        total.append(game())

    return total

if __name__ == "__main__":
    times = int(1e6) # a million games
    attempts = some_games(times)
    print("Average: {:.6f}".format(statistics.mean(attempts)))
    #Average: 0.415761
    print("Std dev: {:.6f}".format(statistics.stdev(attempts)))
    #Std dev: 0.271080
