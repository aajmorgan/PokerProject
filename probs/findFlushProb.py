RIVERMAX = 7
DECKLENGTH = 52
FLUSH = 5
MAXSUIT = 13

def findProb(suits, suitSet, ranks):
    if "flush" in ranks:
        return 1
    elif "fourKind" in ranks:
        return 0
    else:
        cards_to_be_flipped = RIVERMAX - len(suits)
        denom = DECKLENGTH - len(suits)
        for s in suitSet:
            c = suits.count(s)
            if c >= (FLUSH - cards_to_be_flipped):
                if cards_to_be_flipped == 2:
                    temp1 = 1 if c == 4 else (MAXSUIT - c - 1) / (denom - 1)
                    total = (MAXSUIT - c) / denom * temp1
                    temp2 = 0 if c == 3 else ((denom - (MAXSUIT - c)) / denom) * ((MAXSUIT - c) / (denom - 1))
                    return total + temp2
                else:
                    total = (MAXSUIT - c) / denom
                    return total
        return 0

'''
#testing 

s = [2, 2, 3, 3, 3]
s1 = set(s)
ranks = ["n"]
print(findProb(s, s1, ranks))

'''
