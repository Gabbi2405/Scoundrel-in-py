class Card:
    def __init__(self, value:int, suit:str):
        self.value:int = value
        self.suit:str = suit
    
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
        elif value==0:
            value="joker"

        return f"{value} of {self.suit}"
    
    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        suit_order = {'heart': 0, 'diamonds': 1, 'spades': 2, 'clubs': 3}
        if self.suit == other.suit:
            return self.value < other.value
        return suit_order[self.suit] < suit_order[other.suit] 
