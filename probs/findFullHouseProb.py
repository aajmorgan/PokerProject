import math

RIVERMAX = 7
DECKLENGTH = 52
NUMS = 4 # both for individual nums and nums it can't be

def findProb(cards, cardSet, ranks):
    if "fullHouse" in ranks:
        return 1
    elif "pair" not in ranks:
        return 0
    else:
        if "fourKind" in ranks:
            return calculatePair(cards, 4)
        elif 'threeKind' in ranks:
            return calculatePair(cards, 3)
        elif 'twoPair' in ranks:
            return calculateTwoPair(cards)
        else:
            return calculate(cards)

def calculate(cards):
    '''
    We know there is a pair in here, and only a pair
    The pair has to be used in the full house
    There are 2 outcomes with that pair:
        - The pair becomes part of the 3 of a kind
        - The pair stays a pair, and another card becomes a 3 of a kind

    Since this is only if there's a pair, and if there are 6 cards and only 1 pair out
        then getting a full house is impossible, then we know:
        - cards_to_be_flipped = 2
        - if cards_to_be_flipped = 1, return 0
    '''
    cards_to_be_flipped = RIVERMAX - len(cards)
    if cards_to_be_flipped == 1:
        return 0
    total1 = 0
    total2 = 0
    denom = DECKLENGTH - len(cards)

    #only do once
    l = math.comb(len(cards) - 2, 1)

    # start with pair being the three of a kind
    total1 += ((NUMS - 2) / denom) * ((NUMS - 1) / (denom - 1)) # 3rd then 2nd
    #need to check if third card is in either spot
    total1 += ((NUMS - 1) / denom) * ((NUMS - 2) / (denom - 1)) # 2nd then 3rd

    # pair stays pair, other card becomes 3 of a kind
    # that other card needs to be in our set, then in both spots

    total2 += ((NUMS - 1) / denom) * ((NUMS - 2) / (denom - 1))

    return l * (total1 + total2)
        
def calculateTwoPair(cards):
    '''
    With 2 pair, there's a couple of options based on cards_to_be_flipped
        - if 2:
            - one of the next flipped cards has to be one of those in the pair
            - but could also include the single card that isn't a pair, but in order only
                - if [1, 2, 2, 3, 3], then order can only be 1 then 2 or 1 then 3 since if
                3 or 2 went first then there would already be a full house
        - if 1:
            - the last card can only be one of the 2 cards in the two pair, which is 4 cards total
    '''
    cards_to_be_flipped = RIVERMAX - len(cards)
    denom = DECKLENGTH - len(cards)

    # can group either pair getting it's third card into 1
    # so there can be 4 possible cards since both numbers have 2 cards remaining
    NUMERATOR = 4

    if cards_to_be_flipped == 2:
        total = (NUMERATOR / denom) * ((denom - NUMERATOR - 1) / (denom - 1))
        total += ((denom - NUMERATOR) / denom) * (NUMERATOR / (denom - 1))
        # does the denom - NUMERATOR need to be NUMERATOR?
        # as in is it ok if it's one of those 4 or should that be taken off still?
    else:
        # know denom is 46 instead of 47 because of equation above for denom
        total = NUMERATOR / denom

    return total

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
#testing 


cards = [1, 3, 2, 3, 2]
cardSet = set(cards)
ranks = ['pair', 'twoPair']
print(findProb(cards, cardSet, ranks))

#'''
