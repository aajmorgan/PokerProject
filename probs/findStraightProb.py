DECKLENGTH = 52

def findProb(cards, ranks, straightFlush=0):
    suits = 4 if straightFlush == 0 else 1
    if "straight" in ranks:
        return 1
    elif "fourKind" in ranks:
        return 0
    elif "fullHouse" in ranks:
        return 0
    else:
        prob = 0
        num_cards = len(cards) if straightFlush == 0 else straightFlush
        denom = DECKLENGTH - num_cards
        cardsThatWork = []
        cardPairs = []
        for i in range(2, 15):
            cardsCopy = cards[:]
            cardsCopy.append(i)
            if checkStraight(cardsCopy):
                cardsThatWork.append(i)
        print("cardsthatwork", cardsThatWork)
        if num_cards == 5:
            for i in range(2, 14):
                for j in range(i, 15):
                    if i not in cardsThatWork and j not in cardsThatWork:
                        cardsCopy = cards[:]
                        cardsCopy.append(i)
                        cardsCopy.append(j)
                        if checkStraight(cardsCopy):
                            cardPairs.append([i, j])
            nums = []
            for pair in cardPairs:
                for num in pair:
                    nums.append(num)
            numSet = set(nums)
            print("nums", nums)
            print('numSet', numSet)
            temp1 =  (suits / denom) * (suits / (denom - 1))
            temp2 = 0
            for card in numSet:
                temp2 += nums.count(card) 
            prob += temp1 * temp2
            print(prob)
        temp = 0 if num_cards == 6 else (denom - suits) / (denom) * (suits / (denom - 1))
        prob += len(cardsThatWork) * ((suits/denom) + temp)
        
        return prob


def checkStraight(cards):
    numsNoDups = sorted(cards)
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
                            return True
    return False
