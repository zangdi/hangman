from menu import *

print("Welcome to HangMan")

while 1:
    result = menu()
    if result.lower() == 'x':
        print("Seeya later alligator!")
        exit(0)
    elif result == '1':
        single_player()
    elif result == '2':
        multi_player()
    else:
        invalid()
