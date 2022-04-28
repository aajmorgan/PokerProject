import math

from deck_of_cards import deck_of_cards
import pygame

import analyzeCards

pygame.font.init()

KEYS = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_SPACE: 10,
    pygame.K_0: 11,
    pygame.K_e: 12
}

BUTTONWIDTH, BUTTONHEIGHT = 170, 80

CONVERSION = {
        "Pair": "pair",
        "Two Pair": "twoPair",
        "Three of a Kind": "threeKind",
        "Straight": "straight",
        "Flush": "flush",
        "Full House": "fullHouse",
        "Four of a Kind": "fourKind",
        "Straight Flush": "straightFlus",
        "Royal Flush": "royalFlush"
    }

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("arial", 20)


# Returns a shuffled deck of cards
def set_deck():
    deck_obj = deck_of_cards.DeckOfCards()
    deck_obj.shuffle_deck()
    return deck_obj


class Poker:
    def __init__(self, surface):
        self.deck = set_deck()
        self.hand = [self.deck.give_first_card(), self.deck.give_first_card()]
        self.river = [self.deck.give_first_card(), self.deck.give_first_card(), self.deck.give_first_card()]
        self.surface = surface
        self.names = {"Pair": "0%", "Two Pair": "0%", "Three of a Kind": "0%", "Straight": "0%", 
                        "Flush": "0%", "Full House": "0%", "Four of a Kind": "0%", "Straight Flush": "0%",
                        "Royal Flush": "0%"}
        self.surface.fill(0x35654D)
        pygame.event.set_blocked(None)
        pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT, pygame.MOUSEBUTTONDOWN])
        self.buttons = []
        for j in range(4):
            for i in range(3):
                self.buttons.append(pygame.Rect(i * 400 + 15, j * 100 + 15, BUTTONWIDTH, BUTTONHEIGHT))
        pygame.display.update()
        self.buttonTexts = ["(1) Pair", "(2) Two Pair", "(3) Three of a Kind", "(4) Straight", "(5) Flush",
                            "(6) Full House", "(7) Four of a Kind", "(8) Straight Flush", "(9) Royal Flush",
                            "(Space) Next Card", "(0) Simulate", "(e) Choose Card"]

    def checkMouse(self, mouse):
        # check where mouse is clicked, see which action to perform
        gotButton = False
        button = None
        for j in range(4):
            for i in range(3):
                left = i * 400 + 15
                top = j * 100 + 15
                if (mouse[0] in range(left, left + BUTTONWIDTH)) and (mouse[1] in range(top, top + BUTTONHEIGHT)):
                    button = j * 3 + i + 1
                    gotButton = True
                    break
            if gotButton:
                break
        return button

    def drawFirstFive(self):
        self.draw_card(self.hand[0], (385, 800))
        self.draw_card(self.hand[1], (510, 800))
        self.draw_card(self.river[0], (200, 425))
        self.draw_card(self.river[1], (324, 425))
        self.draw_card(self.river[2], (448, 425))
        for i, button in enumerate(self.buttons):
            pygame.draw.rect(self.surface, WHITE, button)
            text = font.render(f"{self.buttonTexts[i]}", True, BLACK, WHITE)
            textRect = text.get_rect()
            textRect.center = button.center
            self.surface.blit(text, textRect)
        pygame.display.update()

    @staticmethod
    def getKey(event):
        if event.key == pygame.K_q:
            pygame.quit()
            quit()
        elif event.key in KEYS:
            return KEYS[event.key]
        else:
            return None

    def play(self):
        running = True
        choice = None
        self.drawFirstFive()
        self.get_probability()
        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                choice = self.getKey(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                choice = self.checkMouse(pygame.mouse.get_pos())
            if choice is not None:
                self.doChoice(choice)
            if len(self.river) == 5:
                running = False
                self.final_result()
        print("Press Space to play again, or q to quit.\n")
        askNextGame = True
        while askNextGame:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    askNextGame = False

    def draw_card(self, card, coords):
        name = "./images/" + card.name.replace(" ", "_") + ".png"
        cardPng = pygame.image.load(name)
        scaledPng = pygame.transform.rotozoom(cardPng, 0, 150 / 726)
        self.surface.blit(scaledPng, coords)
        pygame.display.update()

    def doChoice(self, choice):
        if choice == 10 and len(self.river) < 5:
            self.river.append(self.deck.give_first_card())
            if len(self.river) == 4:
                self.draw_card(self.river[3], (572, 425))
                self.get_probability()
            if len(self.river) == 5:
                self.draw_card(self.river[4], (698, 425))
                self.final_dictionary()
        elif choice == 11:
            self.simulate()
        elif choice == 12:
            self.inputCards()
            
        return False

    @staticmethod
    def num_trials(err=.01, prob=.05):
        # Use chebyshev to find
        trials = math.ceil(.25/((err ** 2) * prob))
        return trials

    def inputCards(self):
        while True:
            try:
                num_cards = int(input("How many cards would you like to input: "))
                while num_cards not in range(1, 7):
                    print("Invalid number of cards. Try again.\n")
                    num_cards = int(input("How many cards would you like to input: "))
                break
            except ValueError:
                print("Invalid input. Try again")
        newDeck = []
        print("\nRanks. 11=Jack, 12=Queen, 13=King, 1=Ace")
        print("Suit. 0=spades, 1=hearts, 2=diamonds, 3=clubs\n")
        while len(newDeck) < num_cards:
            while True:
                print("Type in rank suit (ex: 11 2 for Jack of diamonds)")
                inputList = input().split()
                while len(inputList) != 2:
                    print("Invalid input length. Try again")
                    inputList = input().split()
                suit = inputList[1]
                rank = inputList[0]
                try:
                    suit = int(suit)
                    rank = int(rank)
                    break
                except ValueError:
                    print("\nInvalid input. Type in numbers")
            if suit not in range(0, 4):
                print("\nInvalid suit. 0=spades, 1=hearts, 2=diamonds, 3=clubs")
            elif rank not in range(1, 14):
                print("\nInvalid rank. 11=Jack, 12=Queen, 13=King, 1=Ace")
            else:
                card = deck_of_cards.Card((suit, rank))
                if card not in newDeck:
                    newDeck.append(card)
                    print(card.name)
                    print()
                else:
                    print("\nCard already in deck\n")
        self.deck = set_deck()
        for card in newDeck:
            self.deck.deck.remove(card)
        if len(newDeck) > 2:
            self.hand = newDeck[:2]
            self.river = newDeck[2:]
        else:
            self.hand = newDeck[:]
            self.river = []
            while len(self.hand) < 2:
                self.hand.append(self.deck.give_first_card())
        while len(self.river) < 3:
            self.river.append(self.deck.give_first_card())
        self.surface.fill(0x35654D)
        pygame.display.update()
        self.drawFirstFive()
        if num_cards == 6:
            self.draw_card(self.river[3], (572, 425))
        self.get_probability()
        pygame.display.update()

    def simulate(self):
        print("\nSimulating...\n")
        trials = self.num_trials()
        cards = self.hand + self.river
        counts = {
            "pair": 0,
            "twoPair": 0,
            "threeKind": 0,
            "straight": 0,
            "flush": 0,
            "fullHouse": 0,
            "fourKind": 0,
            "straightFlush": 0,
            "royalFlush": 0
        }
        bests = {
            "highCard": 0,
            "pair": 0,
            "twoPair": 0,
            "threeKind": 0,
            "straight": 0,
            "flush": 0,
            "fullHouse": 0,
            "fourKind": 0,
            "straightFlush": 0,
            "royalFlush": 0
        }
        for i in range(trials):
            num_new_cards = 7 - len(cards)
            for j in range(num_new_cards):
                cards.append(self.deck.give_first_card())
            ranks = self.check_ranks(cards=cards)
            if len(ranks) == 0:
                bests["highCard"] += 1
            else:
                bests[ranks[-1]] += 1
                for rank in ranks:
                    counts[rank] += 1
            for j in range(num_new_cards):
                self.deck.take_card(cards.pop())
            self.deck.shuffle_deck()
        for card in counts:
            counts[card] = f'{round((counts[card] / trials) * 100, 5)} %'
        for card in bests:
            bests[card] = f'{round((bests[card] / trials) * 100, 5)} %'
        print("Counts:", counts)
        print("Bests:", bests)

    def final_result(self):
        hand_ranks = self.check_ranks()
        if len(hand_ranks) == 0:
            print("High card.")
        else:
            # need to choose best hand and print that
            # best_hand = choose_best(hand_ranks)
            print(hand_ranks)
            print(f"You got a {hand_ranks[-1]}!")

    def check_ranks(self, cards=None):
        if cards is None:
            cards = self.hand + self.river
        nums = []
        suits = []
        for card in cards:
            nums.append(card.rank)
            suits.append(card.suit)
        suitSet = set(suits)
        numSet = set(nums)
        return analyzeCards.check_ranks(nums, numSet, suits, suitSet, cards)

    def get_probability(self):
        probs = analyzeCards.findProbabilities(self.hand + self.river)
        for i, k in enumerate(self.names):
            self.names[k] = probs[i]
        print(self.names)

    def final_dictionary(self):
        hand_ranks = self.check_ranks()
        for k in self.names:
            if CONVERSION[k] in hand_ranks:
                self.names[k] = "100%"
            else:
                self.names[k] = "0%"
        print()
        print(self.names)


def main():
    pygame.init()
    surface = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Poker")
    # add while loop to make it so you can play again
    playing = True
    poker = Poker(surface)
    while playing:
        print("You have started a round of poker!")
        poker.play()
        poker = Poker(surface)
    pygame.quit()


if __name__ == '__main__':
    main()
