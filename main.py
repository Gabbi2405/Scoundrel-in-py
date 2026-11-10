from src.entities.card_games.deck import Deck
from src.entities.card_games.cards import Card

from src.entities.scoundrel.room import Room
from src.entities.scoundrel.discard_pile import DiscardPile
from src.entities.scoundrel.hand import Hand



def print_game_status(room:Room, hand:Hand,life:int):
    print("Your life is actually:", life)
    print("Rooom")
    room.print_cards()
    print("Weapon equiped and moster defeated")
    hand.print_cards()

def game():
    deck=Deck()
    room=Room()
    hand=Hand()
    discard=DiscardPile()
    LIFEPOIN_MAX=20
    life=LIFEPOIN_MAX

    room.draw_room(deck)
    print_game_status(room,hand,life)

    while(True):
        if len(room.cards)==4 and not room.runed :
            selected=input("select a card position (1-4), \nor \"run\" to run away from the room\n")
            print(f"[DEBUG] selected value:\n{selected}")
            if selected=="run":
                room.run_away(deck)
            else:
                try:
                    print(type(selected))
                    selected=int(selected)
                    print(type(selected))
                except Error as e:
                    print(f"The imput given is not a number n'or run\nError raised:\n{e}")
                
        else:
            selected=input("select a card position (1-4)")
        if type(selected) != int:
            print("The imput given is not a number")
        if selected>=4 and selected<=1:
            print("The inputed number is not in range")
        room.selct(selected,hand)


if __name__=="__main__":
    game()
    
