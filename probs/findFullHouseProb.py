import math

RIVERMAX = 7
DECKLENGTH = 52
NUMS = 4  # both for individual nums and nums it can't be


def findProb(cards, ranks):
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

    # only do once
    l = math.comb(len(cards) - 2, 1)

    # start with pair being the three of a kind
    total1 += ((NUMS - 2) / denom) * ((NUMS - 1) / (denom - 1))  # 3rd then 2nd
    # need to check if third card is in either spot
    total1 += ((NUMS - 1) / denom) * ((NUMS - 2) / (denom - 1))  # 2nd then 3rd

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
    
    temp = 3 if len(set(cards)) == 3 else 2
    pairs = 2 if len(cards) == 5 else temp

    # can group either pair getting it's third card into 1
    # so there can be 4 possible cards since both numbers have 2 cards remaining

    if cards_to_be_flipped == 2:
        total = (pairs * 2 / denom)
        total += ((denom - (pairs * 2)) / denom) * ((pairs * 2) / (denom - 1))
        # does the denom - NUMERATOR need to be NUMERATOR?
        # as in is it ok if it's one of those 4 or should that be taken off still?
    else:
        # know denom is 46 instead of 47 because of equation above for denom
        total = (pairs * 2) / denom

    return total


def calculatePair(cards, c):
    cards_to_be_flipped = RIVERMAX - len(cards)
    unmatchedCards = len(cards) - c
    denom = DECKLENGTH - len(cards)
    left = NUMS - c  # num cards left in 3 of a kind number
    if cards_to_be_flipped == 2:
        total = (unmatchedCards * ((NUMS - 1) / denom)) + \
                ((denom - (unmatchedCards * 3)) / denom) * ((unmatchedCards * 3) / (denom - 1)) + \
                (((denom - (unmatchedCards * 3) - left) / denom) * (3 / (denom - 1)))
        print(total, (unmatchedCards * ((NUMS - 1) / denom)),  ((denom - (unmatchedCards * 3)) / denom) * ((unmatchedCards * 3) / (denom - 1)), (((denom - (unmatchedCards * 3) - left) / denom) * (3 / (denom - 1))))
    else:
        total = unmatchedCards * (NUMS - 1) / denom
    return total
