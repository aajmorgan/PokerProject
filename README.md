# Installing Modules
To start, you need to pip/pip3 install pygame and deck-of-cards (even though it needs to be imported as deck_of_cards).

# PokerProject
Randomness final project

# Shows probabilities
Specific hands can be placed down and tested on their likeliness of happening. 
poker.py drives the entire program, followed by analyzeCards.py that finds what hands you might already have.
That file also calls all the other probability files, like findPairProb.py, and returns that chance.

# Simulates
poker.py also has a Monte Carlo function, used to both test that the calculated probabilities are right,
but also to see how often a specific hand is the best hand you have, which is the second probability under the line.
