import math

RIVERMAX = 7
DECKLENGTH = 52
NUMS = 4 # both for individual nums and nums it can't be

def findProb(cards, cardSet, ranks):
    if "fullHouse" in ranks:
        return 1
    elif "pair" not in ranks:
        return 0
    elif "threeKind" not in ranks and "twoPair" not in ranks:
        if len(cards) == 6:
            return 0
    else:
        if "fourKind" in ranks:
            return calculatePair(cards, 4)
        elif 'threeKind' in ranks:
            return calculatePair(cards, 3)

def calculate(cards, cardSet):
    cards_to_be_flipped = RIVERMAX - len(cards)
    total = 0
    for card in cardSet:
        c = cards.count(card)
        


def calculatePair(cards, c):
    cards_to_be_flipped = DECKLENGTH - len(cards)
    l = math.comb(len(cards), 1) - c
    denom = DECKLENGTH - len(cards)
    left = NUMS - c # num cards left in 3 of a kind number
    if cards_to_be_flipped == 2:
        total = ((NUMS - 1)/denom) * (denom - (NUMS - 1)  - left - 1)/(denom - 1) + (denom - (NUMS - 1) - left) / (denom) * ((NUMS - 1)/(denom - 1))
    else:
        total = (NUMS - 1)/denom
    adding = 0 if cards_to_be_flipped == 1 else (NUMS / denom) * ((NUMS - 1) / (denom - 1))
    total += adding
    return l * total

'''
testing 


cards = [1, 3, 3, 3, 2]
cardSet = set(cards)
ranks = ['threeKind', 'pair']
print(findProb(cards, cardSet, ranks))

'''
