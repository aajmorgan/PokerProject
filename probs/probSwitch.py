from . import findFlushProb, findFourKindProb, findFullHouseProb, findPairProb, findRoyalFlushProb, \
    findStraightFlushProb, findStraightProb, findThreeKindProb, findTwoPairProb


def probSwitcher(choice, nums, numSet, suits, suitSet, ranks, cards):
    if choice == 1:
        prob = findPairProb.findProb(nums, ranks)
        print(f"Probability of a pair is {round(prob, 6) * 100}%")
    elif choice == 2:
        prob = findTwoPairProb.findProb(nums, numSet, ranks)
        print(f"Probability of a two pair is {round(prob, 6) * 100}%")
    elif choice == 3:
        prob = findThreeKindProb.findProb(nums, numSet, ranks)
        print(f"Probability of a three of a kind is {round(prob, 6) * 100}%")
    elif choice == 4:
        prob = findStraightProb.findProb(cards, ranks)
        print(f"Probability of a straight is {round(prob, 6) * 100}%")
    elif choice == 5:
        prob = findFlushProb.findProb(suits, suitSet, ranks)
        print(f"Probability of a flush is {round(prob, 6) * 100}%")
    elif choice == 6:
        prob = findFullHouseProb.findProb(numSet, ranks)  # could this just be findTwoPair * findThreeKind?
        print(f"Probability of a full house is {round(prob, 6) * 100}%")
    elif choice == 7:
        prob = findFourKindProb.findProb(nums, numSet, ranks)
        print(f"Probability of a four of a kind is {round(prob, 6) * 100}%")
    elif choice == 8:
        prob = findStraightFlushProb.findProb(cards, ranks)
        print(f"Probability of a straight flush is {round(prob, 6) * 100}%")
    elif choice == 9:
        prob = findRoyalFlushProb.findProb(cards, ranks)
        print(f"Probability of a royal flush is {round(prob, 6) * 100}%")
    else:
        prob = -1
        print("Error")
    if prob == 1:
        print("You have it!")
    print()
