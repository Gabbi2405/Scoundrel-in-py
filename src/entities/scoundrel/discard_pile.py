from typing import List
class DiscardPile:
    def __init__(self):
        self.cards:List=[]

    def add_card(self, card:Card):
        self.cards.append(card)

    def print_cards(self):
        self.cards.sort()
        for card in self.cards:
            print(card)
