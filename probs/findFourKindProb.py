def findProb(cards, cardSet, ranks):
    if "fourKind" in ranks:
        return 1
    else:
        if "pair" not in ranks:
            return 0
        needTwo = 2/47 * 1/46
        needOne = 1/47 + 46/47 * 1/46
        if len(cards) == 5:
            if "fullHouse" in ranks:
                prob = needOne + needTwo
            elif "threeKind" in ranks:
                prob = needOne
            elif "twoPair" in ranks:
                prob = needTwo + needTwo
            elif "pair" in ranks:
                prob = needTwo
            else:
                return -1  # Should not be able to return this
           return prob
         else:  # 6 cards
            if "threeKind" not in ranks:
                return 0
            prob = 1 / 46
            if len(cardSet) == 2:
                # This would be for example, your cards are 333 222, can get a 3 or 2
                prob *= 2
            return prob
