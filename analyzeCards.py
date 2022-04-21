from probs import probSwitch

def findProbabilities(choice, cards):
    nums = []
    suits = []
    for card in cards:
        nums.append(card.rank)
        suits.append(card.suit)
    suitSet = set(suits)
    numSet = set(nums)
    ranks = check_ranks(nums, numSet, suits, suitSet, cards)
    probSwitch.probSwitcher(choice, nums, numSet, suits, suitSet, ranks, cards)


def check_ranks(nums, numSet, suits, suitSet, cards):
    ranks = []
    hand_ranks = {
        "pair": False,
        "twoPair": False,
        "threeKind": False,
        "straight": False,
        "flush": False,
        "fullHouse": False,
        "fourKind": False,
        "straightFlush": False,
        "royalFlush": False
    }
    check_all(nums, numSet, suits, suitSet, hand_ranks, cards)
    for rank in hand_ranks:
        if hand_ranks[rank]:
            ranks.append(rank)
    return ranks


def check_all(nums, numSet, suits, suitSet, hand_ranks, cards):
    for num in numSet:
        x = nums.count(num)
        if x >= 2:
            hand_ranks["pair"] = True
        if x >= 3:
            hand_ranks["threeKind"] = True
        if x == 4:
            hand_ranks["fourKind"] = True
    numSetCopy = numSet.copy()
    for num in numSet:
        if nums.count(num) >= 2:
            numSetCopy.remove(num)
            for otherNum in numSetCopy:
                if nums.count(otherNum) >= 2:
                    hand_ranks["twoPair"] = True
                if hand_ranks["twoPair"]:
                    if nums.count(otherNum) >= 3 or nums.count(num) >= 3:
                        hand_ranks["fullHouse"] = True
    for suit in suitSet:
        x = suits.count(suit)
        if x >= 5:
            hand_ranks["flush"] = True
    numsNoDups = sorted(numSet)
    for num in numsNoDups:
        if num == 1:
            numsNoDups.remove(1)
            numsNoDups.append(14)
    numsNoDups = sorted(numSet)
    if len(numsNoDups) >= 5:
        numsNoDups.reverse()
        for i in range(len(numsNoDups) - 4):
            if (numsNoDups[i]-1) == numsNoDups[i+1]:
                if (numsNoDups[i] - 2) == numsNoDups[i+2]:
                    if (numsNoDups[i] - 3) == numsNoDups[i+3]:
                        if (numsNoDups[i] - 4) == numsNoDups[i+4]:
                            hand_ranks["straight"] = True
                            # IDK how to do straight flush and royal flush yet, but royal flush should
                            # just be if its a straight flush with first card being ace (cause I reversed list)



