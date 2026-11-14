from src.entities.card_games.deck import Deck
from src.entities.card_games.cards import Card

from src.entities.scoundrel.room import Room
from src.entities.scoundrel.discard_pile import DiscardPile
from src.entities.scoundrel.hand import Hand



def print_game_status(room:Room, hand:Hand,life:int):
    print("\nYour life is actually:", life)
    print("Rooom:")
    room.print_cards()
    print("Weapon equiped and moster defeated:")
    hand.print_cards()



def check_selection(selected:str, deck:Deck, discard:DiscardPile):
    if selected=="deck":
        print(f"you have still {deck.get_card_number()} card(s) in the deck\n")
        return "CONTINUE"
    elif selected=="discard":
        discard.print_cards()
        return "CONTINUE"
    elif selected=="quit":
        print("it was nice to play with you, byee ;p")
        return "BREAK"
    try:
        selected=int(selected)
    except ValueError:
        print(f"\nThe imput given is not valid\n")
        return "CONTINUE"
    except Exception as e:
        print("Error raised:\n{type(e)}")
        return "BREAK"
    return selected-1

def prepare_deck(deck:Deck):
    '''Rimuove le carte non utili dal mazzo quindi ace jack queen e king di diamonds e heart'''
    for value in [1,11,12,13]:
        for color in ["heart", "diamonds"]:
            deck.remove(value, color)
    deck.shuffle()

def game_over():
    #ToDo
    print("hai perso")

def game():
    deck=Deck()
    prepare_deck(deck)
    room=Room()
    hand=Hand()
    discard=DiscardPile()
    LIFEPOIN_MAX=20
    life=LIFEPOIN_MAX
    room.draw_room(deck)

    while(True):
        print_game_status(room,hand,life)
        if len(room.cards)==4 and not room.runed :
            selected=input(f"select a card position (1-{room.card_number}), \n \"run\" to run away from the room\n \"deck\" to check how many card you have in your deck \n \"discard\" to check your discard pile\n \"quit\" to close the program\n\n")
            #print(f"[DEBUG] selected value:\n{selected}")
            if selected=="run":
                room.run_away(deck)
                continue
            else:
                selected=check_selection(selected, deck, discard)
                if selected=="CONTINUE": continue
                if selected=="BREAK": break
        else:
            selected=input(f"select a card position (1-{room.card_number})\n\n")
            selected=check_selection(selected, deck, discard)
            if selected=="CONTINUE": continue
            if selected=="BREAK": break
        if selected>room.card_number or selected<0:
            print("The inputed number is not in range")
        else:
            life+=room.selct(selected,hand,discard)
            if life>LIFEPOIN_MAX: life=LIFEPOIN_MAX
            elif life<1: 
                game_over()
                break
            room.check(deck)
        
        


if __name__=="__main__":
    game()
    
