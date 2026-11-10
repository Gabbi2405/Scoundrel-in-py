from typing import List

from src.entities.card_games.deck import Deck
from src.entities.scoundrel.hand import Hand



class Room:
    def __init__(self):
        
        self.card_number:int=0
        self.cards:List[:Card]=[]
        self.runed=False
        
    def draw_room(self, deck:Deck):
        CARD_MAX=4
        while self.card_number < CARD_MAX:
            self.cards.append(deck.cards.pop(0))
            self.card_number+=1

    def run_away(self, deck:Deck): 
        if(self.runed):
            shuffle(self.cards)
            while self.cards:
                deck.cards.append(self.cards.pop(0))
            self.cards=[]
            self.draw_room(deck)
            self.runed:bool=True
    
    def selct(self, position:int, hand:Hand):
        pass #fare la selezione della carta
    
    def print_cards(self):
        for card in self.cards:
            print(card)
