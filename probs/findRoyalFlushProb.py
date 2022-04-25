def findProb(cards, ranks):
    if "royalFlush" in ranks:
        return 1
    else:
        suits = []
        cardsCopy = cards[:]
        for card in cards:
            if 1 < card.rank < 10:
                cardsCopy.remove(card)
            else:
                suits.append(card.suit)
        suitSet = set(suits)
        possibleFlushSuit = None
        for suit in suitSet:
            if len(cards) - suits.count(suit) <= 2:
                possibleFlushSuit = suit
                break
        if possibleFlushSuit is None:
            return 0
        newCards = []
        for card in cardsCopy:  # this is the actual cards, not numbers
            if card.suit == possibleFlushSuit:
                newCards.append(card.rank)
        if len(cards) == 5:
            if len(newCards) == 3:
                prob = 2/47 * 1/46
            else:
                prob = 1/47 + 46/47 * 1/46
        else:
            prob = 1/46
        return prob
