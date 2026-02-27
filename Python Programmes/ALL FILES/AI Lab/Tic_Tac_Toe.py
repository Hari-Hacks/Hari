import math

#Initialize board
board = ['' for _ in range(9)]
AI = 'O'
HUMAN = 'X'

#Print board
def print_board():
    print("\n")
    for i in range(3):
        row = ""
        for j in range(3):
            index = 3*i + j
            cell = board[index] if board[index] != "" else str(index)
            row += f" {cell} "
            if j < 2:
                row += "|"
        print(row)
        if i < 2:
            print("---+---+---")
    print("\n")

#Check winner
def check_winner(b):   
    win_states = [
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8], # columns
        [0,4,8],[2,4,6] #diagonals
    ]
    for state in win_states:
        if b[state[0]] == b[state[1]] == b[state[2]] != '':
            return b[state[0]]
    if '' not in b:
        return 'Draw'
    return None
    
#Minimax with Alpha-Beta Pruning
def minimax(b, depth, is_max, alpha, beta):
    winner = check_winner(b)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Draw':
        return 0

    if is_max:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == '':
                b[i] = AI
                eval = minimax(b, depth + 1, False, alpha, beta)
                b[i] = ""
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break #Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == '':
                b[i] = HUMAN
                eval = minimax(b, depth + 1, True, alpha, beta)
                b[i] = ""
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break #Alpha cutoff
        return min_eval

#Find best move for Al
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == '':
            board[i] = AI
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

#Game loop
while True:
    print_board()
    winner = check_winner(board)
    if winner:
        print("Winner:", winner)
        break

    #Human move
    try:
        pos = int(input("Enter position (0-8): "))
        if pos < 0 or pos > 8 or board[pos] != "":
            print("Invalid move. Try again.\n")
            continue
    except:
        print("Invalid input. Enter number 0-8.\n")
        continue

    board[pos] = HUMAN

    #Check winner after human move
    winner = check_winner(board)
    if winner:
        print_board()
        print("Winner:", winner)
        break

    #Al move
    ai_pos = best_move()
    board[ai_pos] = AI
