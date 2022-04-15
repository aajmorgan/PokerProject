import math

RIVERMAX = 7
DECKLENGTH = 52
NUMS = 4 # 1 for each suit

def findProb(nums, ranks):
    if "pair" in ranks:
        return 1
    else:
        return calculate(nums)

def calculate(cards):
    cards_to_be_flipped = RIVERMAX - len(cards)
    l = math.comb(len(cards), 1) # each card has same probability, so only have to do calculation once
    denom = DECKLENGTH - len(cards)
    if cards_to_be_flipped == 2:
        total = ((NUMS - 1)/denom) * (denom - (NUMS - 1) - 1)/(denom - 1) + (denom - 3) / (denom) * ((NUMS - 1)/(denom - 1))
    else:
        total = (NUMS - 1)/denom
    adding = 0 if cards_to_be_flipped == 1 else (NUMS / denom) * ((NUMS - 1) / (denom - 1))
    total += adding
    return l * total

'''
testing below

nums = [1, 2, 3, 4, 5]
ranks = ["p"]
print(findProb(nums, ranks))

'''
