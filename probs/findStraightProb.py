import deck_of_cards

def findProb(cards, cardSet, ranks):
    if "straight" in ranks:
        return 1
    else:
        prob = 0
        sorted_cards = sorted(cards)
        if len(cards) == 5:
            if "fourKind" in ranks:
                return 0
            if "threeKind" in ranks:
                return 0
            #5 in a row already
            if (sorted_cards[4] - sorted_cards[0] + 1) == 5:
                prob = 1
            #4 in a row already
            if (sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4:
                prob = 4/47
            #3 in a row already
            if (sorted_cards[2] - sorted_cards[0] + 1) == 3 or (sorted_cards[4] - sorted_cards[2] + 1) == 3 or (sorted_cards[3] - sorted_cards[1] + 1) == 3:
                prob = 8/47
            #2 in a row already with 1 card one num away
            if "twoKind" in ranks and (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[2] - sorted_cards[1] == 2 or sorted_cards[3] - sorted_cards[2] == 2 or sorted_cards[4] - sorted_cards[3] == 2):
                prob = 12/47
            #if its 4 consecutive even or odd numbers - then the next 2 could fill it in
            if (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[3] - sorted_cards[2] == 2) or (sorted_cards[4] - sorted_cards[3] == 2 or sorted_cards[3] - sorted_cards[2] == 2) or (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[4] - sorted_cards[3] == 2):
                prob = 8/46
                break
            #special cases for 10 and 2 bc of the ace
            if (sorted_cards[0] == 10 or sorted_cars[0] == 2) and ((sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4):
                prob = 4/47
        #if 6 cards 
        else:
            if "fourKind" in ranks:
                return 0
            if "threeKind" in ranks:
                return 0
            #5 in a row already
            if (sorted_cards[4] - sorted_cards[0] + 1) == 5 or (sorted_cards[5] - sorted_cards[1] + 1) == 5:
                prob = 1
            #4 in a row already
            if (sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4 or (sorted_cards[5] - sorted_cards[2] + 1) == 4:
                prob = 8/46
            #3 in a row already
            if (sorted_cards[2] - sorted_cards[0] + 1) == 3 or (sorted_cards[4] - sorted_cards[2] + 1) == 3 or (sorted_cards[3] - sorted_cards[1] + 1) == 3 or (sorted_cards[5] - sorted_cards[3] + 1) == 3:
                prob = 4/46
            #2 in a row already with 1 card one num away
            if "twoKind" in ranks and (sorted_cards[1] - sorted_cards[0] == 2 or sorted_cards[2] - sorted_cards[1] == 2 or sorted_cards[3] - sorted_cards[2] == 2 or sorted_cards[4] - sorted_cards[3] == 2 or sorted_cards[5] - sorted_cards[4] == 2):
                prob = 4/46
            #special cases for 10 and 2 bc of the ace
            if (sorted_cards[0] == 10 or sorted_cars[0] == 2) and ((sorted_cards[3] - sorted_cards[0] + 1) == 4 or (sorted_cards[4] - sorted_cards[1] + 1) == 4):
                prob = 4/46
        return prob
