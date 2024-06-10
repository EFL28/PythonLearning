import random

def initialize_board(): # Iniciliazamos el tablero vacio
    board = [" " for _ in range(9)]
    return board

def display_board(board): # Mostramos el tablero
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def player_input(): # Pedimos la posición al jugador, escribe el índice del tablero donde escribirá
    position = ''
    while position.isdigit() == False or int(position) not in range(1, 10) or board[int(position) - 1] != " ":
        position = input("Enter a position (1-9): ")

        if position.isdigit() == False:
            print("Invalid input. Please enter a number")
        elif int(position) not in range(1, 10):
            print("Invalid input. Please enter a number between 1 and 9")
        elif board[int(position) - 1] != " ":
            print("Position already taken. Please choose another position")

    return int(position)

def check_winner(board, player_1, player_2): # Chequeamos si hay un ganador
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)
    ] # Donde habra 3 en raya
    
    for combination in winning_combinations: # Comprobamos si hay 3 en raya en el tablero
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player_1:
            print("Player 1 wins!")
            return True
        elif board[combination[0]] == board[combination[1]] == board[combination[2]] == player_2:
            print("Player 2 wins!")
            return True
    
    if " " not in board: # Si no hay ganador y el tablero está lleno, es un empate
        print("It's a tie!")
        return True
    return False
    
def decide_first_player(): # Decidimos quien empieza
    return random.choice([1, 2])

def play_again(): # Preguntamos si quieren jugar de nuevo
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        return True
    else:
        return False

def game():
    is_game_over = False
    player_1 = "X"
    player_2 = "O"
    player_1_turn = None
    player_2_turn = None
    # player_1_win = False
    # player_2_win = False

    
    if decide_first_player() == 1:
        player_1_turn = True
        player_2_turn = False
    else:
        player_1_turn = False
        player_2_turn = True
    
    while is_game_over == False:
        display_board(board)
        position = player_input()
        if player_1_turn:
            if board[position - 1] == " ":
                board[position - 1] = player_1
                player_1_turn = False
                player_2_turn = True
        elif player_2_turn:
            if board[position - 1] == " ":
                board[position - 1] = player_2
                player_1_turn = True
                player_2_turn = False
        
        is_game_over = check_winner(board, player_1, player_2)
        
       
# Juego
while True:
    board = initialize_board()
    game()
    if play_again() == False:
        break
    else:
        board = initialize_board()
        continue