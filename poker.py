from deck_of_cards import deck_of_cards
import pygame

import analyzeCards

KEYS = {
    pygame.K_SPACE: 10,
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_0: 11
}

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
        self.surface.fill(0x35654D)
        self.game = True
        pygame.display.update()

    def checkMouse(self, mouse):
        # check where mouse is clicked, see which action to perform
        print(f'Clicked at ({mouse[0]}, {mouse[1]})')

    def draw(self):
        self.draw_card(self.hand[0], (385, 800))
        self.draw_card(self.hand[1], (510, 800))
        self.draw_card(self.river[0], (200, 425))
        self.draw_card(self.river[1], (324, 425))
        self.draw_card(self.river[2], (448, 425))
        if len(self.river) > 3:
            self.draw_card(self.river[3], (572, 425))
        if len(self.river) > 4:
            self.draw_card(self.river[4], (698, 425))   

    def getKey(self, keys):
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if keys[pygame.K_SPACE] and len(self.river) == 5:
            self.game = False
        self.choice = 0
        for k in KEYS:
            if keys[k]:
                self.choice = KEYS[k]
        if self.choice != 0:
            self.ask_user()

    def play(self):
        run = True
        clock = pygame.time.Clock()
        checked = False
        fifth_river = False
        while self.game:
            check = False
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkMouse(pygame.mouse.get_pos())
                if event.type == pygame.KEYUP:
                    self.getKey(keys)
            keys = pygame.key.get_pressed()
            self.draw()
            if len(self.river) == 5 and not checked:
                fifth_river = True
            if fifth_river:
                checked = True
                self.final_result()
                fifth_river = False

    def draw_card(self, card, coords):
        name = "./images/" + card.name.replace(" ", "_") + ".png"
        cardPng = pygame.image.load(name)
        scaledPng = pygame.transform.rotozoom(cardPng, 0, 150 / 726)
        self.surface.blit(scaledPng, coords)
        pygame.display.update()

    def ask_user(self):
        if self.choice == 10 and len(self.river) < 5:
            self.river.append(self.deck.give_first_card())
        elif self.choice == 11:
            self.simulate()
        else:
            self.get_probability(self.choice)
        return False

    def num_trials(self):
        # use chebyshev to find
        trials = 10000
        return trials

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
            counts[card] = f'{round((counts[card]/trials) * 100, 5)} %'
        for card in bests:
            bests[card] = f'{round((bests[card]/trials) * 100, 5)} %'
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

    def get_probability(self, choice):
        analyzeCards.findProbabilities(choice, self.hand + self.river)


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
