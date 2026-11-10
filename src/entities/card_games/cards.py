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
