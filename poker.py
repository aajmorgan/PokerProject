from deck_of_cards import deck_of_cards
import pygame

import analyzeCards


# Returns a shuffled deck of cards
def set_deck():
    deck_obj = deck_of_cards.DeckOfCards()
    deck_obj.shuffle_deck()
    return deck_obj


def print_card_list(cardList):
    for card in cardList:
        print(card.name)


def get_choice():
    choice = input("Choose from the above choices: ")
    print()
    while True:
        try:
            choice = int(choice)
        except ValueError:
            choice = input("Bad Choice. Pick a number 0-9: ")
            continue
        if choice < 0 or choice > 9:
            choice = input("Bad Choice. Pick a number 0-9: ")
        else:
            return choice


def checkQuitPygame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


class Poker:
    def __init__(self, surface):
        self.deck = set_deck()
        self.hand = [self.deck.give_first_card(), self.deck.give_first_card()]
        self.river = [self.deck.give_first_card(), self.deck.give_first_card(), self.deck.give_first_card()]
        self.surface = surface
        self.surface.fill(0x35654D)
        pygame.display.update()

    def play(self):
        drawing = True
        self.print_all()
        if drawing:
            self.draw_card(self.hand[0], (385, 800))
            self.draw_card(self.hand[1], (510, 800))
            self.draw_card(self.river[0], (200, 425))
            self.draw_card(self.river[1], (324, 425))
            self.draw_card(self.river[2], (448, 425))


        fourth_river = False
        while not fourth_river:
            # might have to check for space bar or something to move onto inputting
            # otherwise cannot quit pygame with the X
            checkQuitPygame()
            fourth_river = self.ask_user()
        self.river.append(self.deck.give_first_card())
        self.print_all()
        if drawing:
            self.draw_card(self.river[3], (572, 425))
        fifth_river = False
        while not fifth_river:
            checkQuitPygame()
            fifth_river = self.ask_user()
        self.river.append(self.deck.give_first_card())
        self.print_all()
        if drawing:
            self.draw_card(self.river[4], (698, 425))
        self.final_result()

    def print_all(self):
        print("__________________________")
        print("Hand:")
        print_card_list(self.hand)
        print("\nRiver:")
        print_card_list(self.river)
        print("__________________________")

    def draw_card(self, card, coords):
        name = "./images/" + card.name.replace(" ", "_") + ".png"
        cardPng = pygame.image.load(name)
        scaledPng = pygame.transform.rotozoom(cardPng, 0, 150 / 726)
        self.surface.blit(scaledPng, coords)
        pygame.display.update()

    def ask_user(self):
        print("Choose 0 to flip next card.")
        print("Choose 1 to see the probability of a pair.")
        print("Choose 2 to see the probability of a two pair.")
        print("Choose 3 to see the probability of a three of a kind.")
        print("Choose 4 to see the probability of a straight.")
        print("Choose 5  to see the probability of a flush.")
        print("Choose 6 to see the probability of a full house.")
        print("Choose 7 to see the probability of a four of a kind.")
        print("Choose 8 to see the probability of a straight flush.")
        print("Choose 9 to see the probability of a royal flush.")
        choice = get_choice()
        if choice == 0:
            return True
        self.get_probability(choice)
        return False

    def final_result(self):
        hand_ranks = self.check_ranks()
        if len(hand_ranks) == 0:
            print("High card.")
        else:
            # need to choose best hand and print that
            # best_hand = choose_best(hand_ranks)
            print(hand_ranks)
            print(f"You got a {hand_ranks[-1]}!")

    def check_ranks(self):
        cards = self.hand + self.river
        nums = []
        suits = []
        for card in cards:
            nums.append(card.rank)
            suits.append(card.suit)
        suitSet = set(suits)
        numSet = set(nums)
        return analyzeCards.check_ranks(nums, numSet, suits, suitSet)

    def get_probability(self, choice):
        print(analyzeCards.findProbabilities(choice, self.hand + self.river))


def main():
    pygame.init()
    surface = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Poker")
    # add while loop to make it so you can play again
    playing = True
    while playing:
        print("You have started a round of poker!")
        poker = Poker(surface)
        poker.play()
        if input("Type q to quit, or anything else to play again. ") == "q":
            playing = False
    pygame.quit()


if __name__ == '__main__':
    main()
