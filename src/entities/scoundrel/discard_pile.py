from typing import List
class DiscardPile:
    def __init__(self):
        self.cards:List=[]

    def print_cards(self):
        for card in self.cards:
            print(card)
