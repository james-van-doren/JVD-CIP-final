import numpy as np

from scipy.stats import hypergeom

import matplotlib.pyplot as plt

def main():
    # get values from user input on sample size, poulation size, etc. and convert to integer

    print('CARD DRAWING ODDS CALCULATOR')
    cards_value = int(input('How many cards are you drawing? '))
    success_value = int(input('How many copies of the desired card are currently in the deck? '))
    copies_value = int(input('How many copies of the desired card do you need to draw? '))
    deck_value = int(input('How many total cards are currently in the deck? '))

    # perform math on the user inputs to calculate odds
    



if __name__ == "__main__":
    main()