from probs import findFlushProb, findFourKindProb, findFullHouseProb, findPairProb, findRoyalFlushProb, \
    findStraightFlushProb, findStraightProb, findThreeKindProb, findTwoPairProb


def findProbabilities(cards):
    nums = []
    suits = []
    for card in cards:
        nums.append(card.rank)
        suits.append(card.suit)
    suitSet = set(suits)
    numSet = set(nums)
    ranks = check_ranks(nums, numSet, suits, suitSet, cards)
    allProbs = [f"{round(findPairProb.findProb(nums, ranks) * 100, 6)}%",
                f"{round(findTwoPairProb.findProb(nums, numSet, ranks) * 100, 6)}%",
                f"{round(findThreeKindProb.findProb(nums, numSet, ranks) * 100, 6)}%",
                f"{round(findStraightProb.findProb(nums, ranks) * 100, 6)}%",
                f"{round(findFlushProb.findProb(suits, suitSet, ranks) * 100, 6)}%",
                f"{round(findFullHouseProb.findProb(nums, ranks) * 100, 6)}%",
                f"{round(findFourKindProb.findProb(nums, numSet, ranks) * 100, 6)}%",
                f"{round(findStraightFlushProb.findProb(cards, suits, suitSet, ranks) * 100, 6)}%",
                f"{round(findRoyalFlushProb.findProb(cards, ranks) * 100, 6)}%"]
    print()
    return allProbs


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
    flushSuit = None
    for suit in suitSet:
        x = suits.count(suit)
        if x >= 5:
            hand_ranks["flush"] = True
            flushSuit = suit
    numsNoDups = sorted(numSet)
    for num in numsNoDups:
        if num == 1:
            numsNoDups.remove(1)
            numsNoDups.append(14)
    numsNoDups = sorted(numsNoDups)
    if len(numsNoDups) >= 5:
        numsNoDups.reverse()
        for i in range(len(numsNoDups) - 4):
            if (numsNoDups[i] - 1) == numsNoDups[i + 1]:
                if (numsNoDups[i] - 2) == numsNoDups[i + 2]:
                    if (numsNoDups[i] - 3) == numsNoDups[i + 3]:
                        if (numsNoDups[i] - 4) == numsNoDups[i + 4]:
                            hand_ranks["straight"] = True
                            break
    cardsCopy = cards[:]
    if hand_ranks['flush'] and hand_ranks["straight"]:
        for card in cards:
            if card.suit != flushSuit:
                cardsCopy.remove(card)
        if len(cardsCopy) >= 5:
            newNums = []
            for card in cardsCopy:
                newNums.append(card.rank)
            for num in newNums:
                if num == 1:
                    newNums.remove(1)
                    newNums.append(14)
            newNums = sorted(newNums)
            newNums.reverse()
            for i in range(len(newNums) - 4):
                if (newNums[i] - 1) == newNums[i + 1]:
                    if (newNums[i] - 2) == newNums[i + 2]:
                        if (newNums[i] - 3) == newNums[i + 3]:
                            if (newNums[i] - 4) == newNums[i + 4]:
                                hand_ranks["straightFlush"] = True
                                if newNums[i] == 14:
                                    hand_ranks["royalFlush"] = True
                                break
