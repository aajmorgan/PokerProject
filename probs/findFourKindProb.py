def findProb(cards, cardSet, ranks):
    if "fourKind" in ranks:
        return 1
    else:
        if "pair" not in ranks:
            return 0
        diffRanks = len(cardSet)
        if len(cards) == 5:
            if "threeKind" not in ranks:
                # Ex 22 3 4 5, or 22 33 4
                if diffRanks == 4:
                    prob = 2 / 47 * 1 / 46
                elif diffRanks == 3:
                    prob = 4 / 47 * 1 / 46
                else:
                    return -1  # should not be able to get
                return prob
            else:
                # Ex 222 33 or 222 3 4
                if diffRanks == 3:
                    prob = 46 / 47 * 1 / 46 + 1 / 47 * 46 / 46  # 46/46 because can be any card, just show work for now
                elif diffRanks == 2:
                    # add prob of the pair ending as four of a kind
                    prob = 1 / 47 * 46 / 46 + 2 / 47 * 2 / 46 + 44 / 7 * 1 / 46
                else:
                    return -1  # should not be able to get
                return prob
        else:  # 6 cards
            if "threeKind" not in ranks:
                return 0
            prob = 1 / 46
            if diffRanks == 2:
                # This would be for example, your cards are 333 222, can get a 3 or 2
                prob *= 2
            return prob
