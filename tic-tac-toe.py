# Vincent Baxter | Ponder & Prove - Tic Tac Toe

def main():
    placedPieces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    validOptions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    chosenSpace = 0
    player = "O"
    gameRunning = True
    turns = 0
    print("""Welcome to Tic Tac Toe
Take turns chosing a square in which to place your piece by entering a number from 1-9 as shown in the example below""")
    drawGrid(placedPieces)
    print()
    input("Press enter to begin")
    placedPieces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print()
    drawGrid(placedPieces)
    print()
    while gameRunning:
        piecePlaced = False
        if player == "X":
            player = "O"
        elif player == "O":
            player = "X"
        try:
            chosenSpace = int(input(f"It is {Fore.GREEN}{player}'s{Style.RESET_ALL} turn! ")) - 1
        except ValueError:
            chosenSpace = -1
        while piecePlaced == False:
            if chosenSpace in validOptions and placedPieces[chosenSpace] == " ":
                placePiece(placedPieces, chosenSpace, player)
                drawGrid(placedPieces)
                piecePlaced = True
            else:
                try:
                    chosenSpace = int(input("Invalid space selected, please try again: ")) - 1
                except ValueError:
                    chosenSpace = -1
        turns += 1
        winner = checkState(placedPieces, player, turns)
        if winner == "":
            pass
        elif winner == "draw":
            gameRunning = False
            print("It's a draw, nobody wins!")
        else:
            gameRunning = False
            print(f"Congratulations player {player}, you are the winner!")

def drawGrid(placedPieces):
    print(f"""
 {placedPieces[0]} | {placedPieces[1]} | {placedPieces[2]}
───┼───┼───
 {placedPieces[3]} | {placedPieces[4]} | {placedPieces[5]}
───┼───┼───
 {placedPieces[6]} | {placedPieces[7]} | {placedPieces[8]}
    """)

def placePiece(placedPieces, chosenSpace, player):
    placedPieces[chosenSpace] = player
    return placedPieces

def checkState(placedPieces, player, turns):
    if placedPieces[0] == placedPieces[1] and placedPieces[1] == placedPieces[2] and placedPieces[0] != " ":
        winner = player
    elif placedPieces[3] == placedPieces[4] and placedPieces[4] == placedPieces[5] and placedPieces[3] != " ":
        winner = player
    elif placedPieces[6] == placedPieces[7] and placedPieces[7] == placedPieces[8] and placedPieces[6] != " ":
        winner = player
    elif placedPieces[0] == placedPieces[3] and placedPieces[3] == placedPieces[6] and placedPieces[0] != " ":
        winner = player
    elif placedPieces[1] == placedPieces[4] and placedPieces[4] == placedPieces[7] and placedPieces[1] != " ":
        winner = player
    elif placedPieces[2] == placedPieces[5] and placedPieces[5] == placedPieces[8] and placedPieces[2] != " ":
        winner = player
    elif placedPieces[0] == placedPieces[4] and placedPieces[4] == placedPieces[8] and placedPieces[0] != " ":
        winner = player
    elif placedPieces[2] == placedPieces[4] and placedPieces[4] == placedPieces[6] and placedPieces[2] != " ":
        winner = player
    elif turns == 9:
        winner = "draw"
    else:
        winner = ""
    return winner

if __name__ == "__main__":
    main()