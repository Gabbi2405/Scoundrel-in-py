
from typing import List
from random import shuffle
from typing import List

class Card:
    def __init__(self, value:int, color:str):
        self.value:int = value
        self.color:str = color
    
    def __str__(self):
        value=self.value
        if value==11:
            value="Jack"
        elif value==12:
            value="Queen"
        elif value==13:
            value="King"
        elif value==1:
            value="Ace"

        return f"{value} of {self.color}"
    
    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value and self.color == other.color

    def __lt__(self, other):
        suit_order = {'heart': 0, 'diamonds': 1, 'spades': 2, 'clubs': 3}
        if self.color == other.color:
            return self.value < other.value
        return suit_order[self.color] < suit_order[other.color] 

class Deck:
    def __init__(self):
        self.cards: List[Card] = [Card(value, color) for value in range(1, 14) for color in ['heart', 'diamonds', 'spades', 'clubs']]
        '''Rimuove le carte non utili dal mazzo quindi ace jack queen e king di diamonds e heart'''
        for value in [1,11,12,13]:
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

class Hand:
    def __init__(self):
        self.cards:List=[]

    def list_cards(self):
        for card in self.cards:
            print(card) 
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
    
    def list_cards(self):
        for card in self.cards:
            print(card)



class Discard_pile:
    def __init__(self):
        self.cards:List=[]

    def list_cards(self):
        for card in self.cards:
            print(card)

def print_game_status(room:Room, hand:Hand,life:int):
    print("Your life is actually:", life)
    print("Rooom")
    room.list_cards()
    print("Weapon equiped and moster defeated")
    hand.list_cards()

def game():
    deck=Deck()
    room=Room()
    hand=Hand()
    discard=Discard_pile()
    LIFEPOIN_MAX=20
    life=LIFEPOIN_MAX

    room.draw_room(deck)
    print_game_status(room,hand,life)

    while(True):
        if len(room.cards)==4 and not room.runed :
            selected=input("select a card position (1-4), or run to run away from the room")
            if selected=="run":
                room.run_away(deck)
            elif type(selected) != "int":
                print("The imput given is not a number n'or run")
        else:
            selected=input("select a card position (1-4)")
        if type(selected) != "int":
            print("The imput given is not a number")
        if selected>4 or selected<1:
            print("The inputed number is not in range")
        room.selct(selected,hand)


if __name__=="__main__":
    game()
    
