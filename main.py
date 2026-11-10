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



def check_selection(selected:str):
    try:
        selected=int(selected)
    except ValueError:
        print(f"\nThe imput given is not valid\n")
        return "CONTINUE"
    except Exception as e:
        print("Error raised:\n{type(e)}")
        return "BREAK"
    return selected



def game():
    deck=Deck()
    room=Room()
    hand=Hand()
    discard=DiscardPile()
    LIFEPOIN_MAX=20
    life=LIFEPOIN_MAX
    room.draw_room(deck)


    while(True):
        print_game_status(room,hand,life)
        if len(room.cards)==4 and not room.runed :
            selected=input("select a card position (1-4), \nor \"run\" to run away from the room\n")
            #print(f"[DEBUG] selected value:\n{selected}")
            if selected=="run":
                room.run_away(deck)
                continue
            else:
                selected=check_selection(selected)
                if selected=="CONTINUE": continue
                if selected=="BREAK": break
        else:
            selected=input("select a card position (1-4)")
            selected=check_selection(selected)
            if selected=="CONTINUE": continue
            if selected=="BREAK": break
        if selected>=4 and selected<=1:
            print("The inputed number is not in range")
        room.selct(selected,hand)


if __name__=="__main__":
    game()
    
