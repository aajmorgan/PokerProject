import deck_of_cards
DECKLENGTH = 52
def findProb(cards, ranks, straightFlush=0):
    SUITS = 4 if straightFlush == 0 else 1
    if "straight" in ranks:
        return 1
    elif "fourKind" or "fullHouse" in ranks:
        return 0
    else:
        prob = 0
        poss_cards = 0
        poss_cards_b = 0
        num_cards = len(cards) if straightFlush == 0 else straightFlush
        numsNoDups = set(sorted(cards))
        sorted_cards = list(numsNoDups)
        for num in sorted_cards:
            if num == 1:
                sorted_cards.remove(1)
                sorted_cards.append(14)
        denom = DECKLENGTH - num_cards
        formula = ((poss_cards*SUITS)/denom)*(((poss_cards -1)*SUITS)/(denom-1))
        otherform = ((poss_cards_b*SUITS)/denom)*((poss_cards_b*(SUITS-1))*(denom-1))
        for card in sorted_cards:
            index = 0
            cardseq = 0
            everyother = 0
            curcard = card
            nextcard = sorted_cards[index+1]
            if nextcard == curcard -1:
                cardseq += 1
            if nextcard == curcard-2:
                everyother += 1
            index += 1
        if num_cards == 5:
            if cardseq <= 2:
                prob = 0
            #need 2 on one side, 2 on other side, 1 on each side
            if cardseq == 3:
                poss_cards = 2
                prob = 3*formula
            #need 1(can be on either side), 2 on one side, 2 on other side
            if cardseq == 4:
                poss_cards = 2
                poss_cards_b = 1
                prob = 2*formula + 2*otherform
            #need 1 in gap with 1 on one side, 1 in gap 1 on other side
            if cardseq == 2 and everyother == 1:
                poss_cards_b = 1
                prob = otherform
            #need 1 in gap, 2 on one side, 1 in gap 1 on other side 
            if cardseq == 3 and everyother == 1:
                poss_cards = 2
                poss_cards_b = 1
                prob = 2*formula + otherform
        #if 6 cards 
        else:
            num_cards = 6
            if cardseq <= 3:
                prob = 0
            #need 1 on either side 
            if cardseq == 4:
                poss_cards = 2
                prob = formula
            #need 1 in gap
            if cardseq == 3 and everyother == 1:
                poss_cards_b = 1
                prob = otherform
        return prob

