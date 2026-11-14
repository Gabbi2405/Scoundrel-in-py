from typing import List

from src.entities.card_games.deck import Deck
from src.entities.card_games.cards import Card
from src.entities.scoundrel.hand import Hand
from src.entities.scoundrel.discard_pile import DiscardPile


class Room:
    def __init__(self):
        
        self.card_number:int=0
        self.cards:List[Card]=[]
        self.runed=False
        
    def draw_room(self, deck:Deck):
        CARD_MAX=4
        while self.card_number < CARD_MAX:
            self.cards.append(deck.cards.pop(0))
            self.card_number+=1
        self.runed=False

    def run_away(self, deck:Deck): 
        if(not self.runed):
            deck.cards.extend(self.cards)
            self.cards.clear()
            self.card_number=0
            self.draw_room(deck)
            self.runed:bool=True
    
    def selct(self, position:int, hand:Hand, discard:DiscardPile):
        selected_card:Card=self.cards[position]
        self.cards.remove(selected_card)
        self.card_number -=1
        self.runed=True
        card_value=selected_card.value
        if card_value==1: card_value=14
        if selected_card.suit=="diamonds":
            hand.equip(selected_card, discard)
            return 0
        elif selected_card.suit=="heart":
            discard.add_card(selected_card)
            return card_value
        elif hand.weapon:
            if not hand.card_number==0:
                last_defeated_value=hand.cards[hand.card_number-1].value
                if last_defeated_value==1: last_defeated_value=14
            
            if hand.card_number==0 or card_value< last_defeated_value :
                hand.add_card(selected_card)
                res=hand.weapon.value - card_value
                if res>=0: return 0
                return res
                
        discard.add_card(selected_card)
        return - selected_card.value
                
        
    
    def check(self, deck:Deck):
        if self.card_number == 1:
            self.draw_room(deck)
    
    def print_cards(self):
        for card in self.cards:
            print(card)
