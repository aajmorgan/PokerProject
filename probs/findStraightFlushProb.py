from . import findStraightProb as straight

RIVERMAX = 7
DECKLENGTH = 52
FLUSH = 5
MAXSUIT = 13

def findProb(cards, suits, suitSet, ranks):
    if "straightFlush" in ranks:
        return 1
    else:
        x = None
        suitNum = 3 if len(cards) == 5 else 4
        newCards = []
        for suit in suitSet:
            if suits.count(suits) >= suitNum:
                x = suit
        if x != None:
            for card in cards: #this is the actual cards, not numbers
                if card.suit == x:
                    newCards.append(card.rank)
            straight.findProb(newcards, set(newCards), ranks)
        return 0 #none of the suits had enough in the hand
