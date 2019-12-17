from run_game import game_choose_word, play_game, player_choose_word
from os import system

def menu():
    print("""            MENU
            1. Single Player
            2. Multi Player
            x. Exit\n\n""")
    return input("Select an option: ")

def single_player():
    print("You're playing by yourself")
    word = game_choose_word()
    winner = play_game(word)
    if winner == 0:
        print("You lost :(\nThe word was", word)
    else:
        print("You won!!!")

def multi_player():
    print("You're playing with a friend")
    word = player_choose_word()
    system("cls")
    winner = play_game(word)
    if winner == 0:
        print("The chooser won!!")
    else:
        print("The guesser won!!")

def invalid():
    print("You have entered an invalid key.\nPlease select an option from the menu")