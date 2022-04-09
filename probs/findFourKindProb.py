import deck_of_cards


def findProb(cards, ranks):
    if "fourKind" in ranks:
        return 1
    else:
        return -1  # TODO: calculate this
