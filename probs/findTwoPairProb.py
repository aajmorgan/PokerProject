import deck_of_cards

def findProb(nums, numSet, ranks):

    if "twoPair" in ranks:
        return 1
    elif "pair" in ranks:
        prob = calculate(numSet, nums)
    else:
        if len(nums) == 5:
            prob = (len(nums)* 3 / 47) * ((len(nums) - 1) * 3) / 46
        else:
            prob = 0
    return prob

def calculate(numSet, nums):
    u = len(numSet) - 1
    prob = (3 * u / 46)
    if len(nums) == 5:   
        prob = (3 * u/47) + ((47-(3 * u)) / 47) * (prob + 3/46)
    return prob

                
