import deck_of_cards
DECKLENGTH = 52
def findProb(cards, ranks, straightFlush=0):
    SUITS = 4 if straightFlush == 0 else 1
    if "straight" in ranks:
        return 1
    else:
        prob = 0
        num_cards = len(cards) if straightFlush == 0 else straightFlush
        sorted_cards = sorted(cards)
        denom = DECKLENGTH - num_cards
        if num_cards == 5:
            poss_cards = 0
            if "fourKind" in ranks:
                return 0
            #4 in a row already, can be in 2 places 
            if (sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4:
                poss_cards = 2
                prob = (poss_cards*SUITS)/(denom-1)
            #3 in a row already, can be in 2 places
            if (sorted_cards[2] - sorted_cards[0] + 1) == 3 or (sorted_cards[4] - sorted_cards[2] + 1) == 3 or (sorted_cards[3] - sorted_cards[1] + 1) == 3:
                poss_cards = 2
                prob = (poss_cards*SUITS)/denom * ((poss_cards-1)*SUITS)/(denom-1)
            #2 in a row already with 1 card one num away, can be in 3 places
            if "twoKind" in ranks and (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[2] - sorted_cards[1] == 2 or sorted_cards[3] - sorted_cards[2] == 2 or sorted_cards[4] - sorted_cards[3] == 2):
                poss_cards = 3
                prob = (poss_cards*SUITS)/denom
            #if its 4 consecutive even or odd numbers - then the next 2 could fill it in
            if (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[3] - sorted_cards[2] == 2) or (sorted_cards[4] - sorted_cards[3] == 2 or sorted_cards[3] - sorted_cards[2] == 2) or (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[4] - sorted_cards[3] == 2):
                poss_cards = 2 
                prob = (poss_cards*SUITS)/(denom-1)
            #special cases for 10 and 2 bc of the ace, can only be in 1 place
            if (sorted_cards[0] == 10 or sorted_cars[0] == 2) and ((sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4):
                poss_cards = 1
                prob = (SUITS*poss_cards)/denom
        #if 6 cards 
        else:
            if "fourKind" in ranks:
                return 0
            if "threeKind" in ranks:
                return 0
            #4 in a row already, can be in 2 places 
            if (sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4 or (sorted_cards[5] - sorted_cards[2] + 1) == 4:
                poss_cards = 2 
                prob = (poss_cards*SUITS)/(denom-1)
            #special cases for 10 and 2 bc of the ace
            if (sorted_cards[0] == 10 or sorted_cars[0] == 2) and ((sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4):
                poss_cards = 1
                prob = (SUITS*poss_cards)/denom
            #if 3 in a row or less, no chance of getting a straight 
            else:
                prob = 0   
        return prob
