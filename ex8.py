__author__ = 'joao'

has_winner = False

while has_winner == False:

    print("1 - Rock")
    print("2 - Papper")
    print("3 - Scissors")

    player_1 = input("player 1:")
    while player_1 != "1" and player_1 != "2" and player_1 != "3":
        player_1 = input("player 1:")

    player_2 = input("player 2:")
    while player_2 != "1" and player_2 != "2" and player_2 != "3":
        player_2 = input("player 2:")

    if (player_1 == "1" and player_2 == "3") or (player_1 == "2" and player_2 == "1") or (player_1 == "3" and player_2 == "2"):
        print("player 1 win!")
        has_winner = True

    if (player_2 == "1" and player_1 == "3") or (player_2 == "2" and player_1 == "1") or (player_2 == "3" and player_1 == "2"):
        print("player 2 win!")
        has_winner = True 



