from menu import menu, single_player, multi_player, invalid

print(""" _______________________________________________________________________________
|                                      ____                                     |
|    |      |      /\     |\     |    /    \    |\    /|     /\     |\     |    |
|    |      |     /  \    | \    |   /          | \  / |    /  \    | \    |    |
|    |______|    /____\   |  \   |  |           |  \/  |   /____\   |  \   |    |
|    |      |   |      |  |   \  |  |      ___  |      |  |      |  |   \  |    |
|    |      |   |      |  |    \ |   \     /|   |      |  |      |  |    \ |    |
|    |      |   |      |  |     \|    \___/ |   |      |  |      |  |     \|    |
|_______________________________________________________________________________|
""")

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