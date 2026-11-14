from random import shuffle

from src.entities.card_games.cards import Card 

class Deck:
    def __init__(self):
        self.cards: List[Card] = [Card(value, color) for value in range(1, 14) for color in ['heart', 'diamonds', 'spades', 'clubs']]

        shuffle(self.cards)
        self.card_number=52
        self.joker_number=0

    def __str__(self):
        return f"cards: {self.cards}"
    
    def list_cards(self):
        for card in self.cards:
            print(card)

    def sort(self):
        self.cards.sort()

    def add_card(self,catd:Card):
        self.cards.append(card)
        self.card_number+=1

    def remove(self, value:int, color:str)->None:
        card= Card(value, color)
        if card in self.cards:
            self.cards.remove(card)
            self.card_number-=1

    def draw_specific_card(self, value:int, color:str)->Card:
        card=Card(value,color)
        if card in  self.cards:
            self.remove(value, color)
            self.card_number-=1
            return card
        else:   
            raise IndexError("Card not in Deck")
    
    def pop_first(self)->Card:
        if self.cards: #check if cards is empty
            self.card_number-=1
            return self.cards.pop(0)
        #else:
            #raise Exception("No more card in the deck")
            return -1
    def get_card_number(self):
        return self.card_number

    def shuffle(self)->None:
        shuffle(self.cards)
        
    def create_joker(self):
        if joker_number==0:
            new_joker=Card(0,"heart")
            self.joker_number+=1
            return new_joker
            
        elif joker_number==1:
            new_joker=Card(0,"heart")
            self.joker_number+=1
            return new_joker
        else:
            raise Exception("All jokers already created")
        
    def add_joker(self):
        joker=self.create_joker()
        if joker:
            self.add_card(joker)