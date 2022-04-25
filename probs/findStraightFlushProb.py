import deck_of_cards
DECKLENGTH = 52

def findProb(card, cardSet, ranks):
    if "straightFlush" in ranks:
        return 1
    else:
        if "Flush" in ranks:
            if "Straight" in ranks:
                prob = 1/(DECKLENGTH - len(cardSet))
        else:
            return 0
