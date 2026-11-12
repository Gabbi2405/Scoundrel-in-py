from src.entities.card_games.cards import Card
from src.entities.scoundrel.discard_pile import DiscardPile

from typing import List

class Hand:
    def __init__(self):
        self.weapon:Card=None
        self.cards:List[Card]=[]
        self.card_number:int=0
        
        
    def equip(self, card:Card, discard:DiscarPile):#ToDo check per scartare larma e i mostri sconfitti in precedenza
        if(self.weapon!=None): 
            discard.cards.extend(self.cards)
            discard.cards.append(self.weapon)
            self.cards.clear()
            self.card_number=0
        self.weapon=card

    def add_card(self, card:Card):
        self.cards.append(card)
        self.card_number+=1

    def print_cards(self):
        print(f"weapon equiped: {self.weapon}\nmoster(s) defeated:")
        for card in self.cards:
            print(card) 
            
            