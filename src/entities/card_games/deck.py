from random import shuffle

from src.entities.card_games.cards import Card 

class Deck:
    def __init__(self):
        self.cards: List[Card] = [Card(value, color) for value in range(1, 14) for color in ['heart', 'diamonds', 'spades', 'clubs']]
        '''Rimuove le carte non utili dal mazzo quindi ace jack queen e king di diamonds e heart'''
        for value in [1,11,12,13]: #ToDo questo andrebbe spostato nella loggica di scoundrel se si vogiono fare altri giochi di carte
            for color in ["heart", "diamonds"]:
                self.remove(value, color)
        shuffle(self.cards)

    def __str__(self):
        return f"cards: {self.cards}"
    
    def list_cards(self):
        for card in self.cards:
            print(card)

    def sort(self):
        self.cards.sort()

    def remove(self, value:int, color:str)->None:
        card= Card(value, color)
        if card in self.cards:
            self.cards.remove(card)

    def pop(self, value:int, color:str)->Card:
        card_to_pop=Card(value,color)
        if card_to_pop in  self.cards:
            self.remove(card_to_pop)
            return card_to_pop
        else:   
            raise IndexError("Card not in Deck")
    
    def pop_first(self)->Card:
        return self.cards.pop(0)

    def shuffle(self)->None:
        shuffle(self.cards)