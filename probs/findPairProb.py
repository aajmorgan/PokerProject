import math

RIVERMAX = 7
DECKLENGTH = 52

def findProb(nums, ranks):
    if "pair" in ranks:
        return 1
    else:
        return calculate(nums)

def calculate(cards):
    cards_to_be_flipped = RIVERMAX - len(cards)
    l = math.comb(RIVERMAX - cards_to_be_flipped, 1)
    adding = 0
    for i in range(cards_to_be_flipped):
        adding += 3/(DECKLENGTH - len(cards) - i)
    return l * adding

'''
testing below

nums = [1, 2, 3, 4, 5]
ranks = ["p"]
print(findProb(nums, ranks))

'''