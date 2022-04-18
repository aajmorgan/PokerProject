import deck_of_cards
RIVERMAX = 7
DECKLENGTH = 52
FLUSH = 5
MAXSUIT = 13

def findProb(card, cardSet, suits, suitSet, ranks):
    if "straightFlush" in ranks:
        return 1
    else:
        cards_to_be_flipped = RIVERMAX - len(suits)
        total = 0
        for card in cardSet:
            if card = card -1:
                for s in suitSet:
                    c = suits.count(s)
                    t1 = 1 if cards_to_be_flipped == 1 else (MAXSUIT - c - 1) / (DECKLENGTH - len(suits) - 1)
                    t2 = 0 if cards_to_be_flipped == 1 else (MAXSUIT - c) / (DECKLENGTH - len(suits) - 1)
                    t2 *= (DECKLENGTH - MAXSUIT - (len(suits) - c)) / (DECKLENGTH - len(suits))
                    print('t2:', t2)
                    if c == FLUSH - cards_to_be_flipped:
                        total = (MAXSUIT - c) / (DECKLENGTH - len(suits)) * t1
                        break
                    elif c > FLUSH - cards_to_be_flipped:
                        total = (MAXSUIT - c) / (DECKLENGTH - len(suits)) * ((DECKLENGTH - MAXSUIT - (len(suits) - c)) / (DECKLENGTH - len(suits) - 1))
                        total += t2
                        break
                return total
            else:
                return 0
