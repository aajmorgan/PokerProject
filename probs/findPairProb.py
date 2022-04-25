RIVERMAX = 7
DECKLENGTH = 52
NUMS = 4 # 1 card for each suit

def findProb(nums, ranks):
    if "pair" in ranks:
        return 1
    else:
        return calculate(nums)

def calculate(cards):
    cards_to_be_flipped = RIVERMAX - len(cards)
    denom = DECKLENGTH - len(cards)
    if cards_to_be_flipped == 2:
        total = ((len(cards) * 3) / denom) + (denom - (len(cards) * 3)) / (denom) * (((len(cards) + 1) * 3)/(denom - 1))
    else:
        total = (len(cards) * 3) / denom
    return total

'''
testing below

nums = [1, 2, 3, 4, 5]
ranks = ["p"]
print(findProb(nums, ranks))

'''
