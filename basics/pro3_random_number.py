import random
import datetime
import time


def random_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    print(f"Random Number: {random_number}")

    # Generate a random float between 0 and 1
    random_float = random.random()
    print(f"Random Float: {random_float}")

    # Generate a random choice from a list
    choices = ['apple', 'banana', 'cherry']
    random_choice = random.choice(choices)
    print(f"Random Choice: {random_choice}")

    # Shuffle a list randomly
    deck_of_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    random.shuffle(deck_of_cards)
    print(f"Shuffled Deck of Cards: {deck_of_cards}")

random_number()