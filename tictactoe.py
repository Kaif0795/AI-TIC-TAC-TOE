import math

def print_board(b):
    for r in b:
        print(" | ".join(r))
    print()

def check_winner(b):
    for r in b:
        if r[0] == r[1] == r[2] and r[0] != '_':
            return r[0]
    for c in range(3):
        if b[0][c] == b[1][c] == b[2][c] and b[0][c] != '_':
            return b[0][c]
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != '_':
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != '_':
        return b[0][2]
    return None

def minimax(b, depth, is_max, alpha, beta):
    winner = check_winner(b)
    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    elif all(b[r][c] != '_' for r in range(3) for c in range(3)):
        return 0

    if is_max:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == '_':
                    b[r][c] = 'X'
                    best = max(best, minimax(b, depth + 1, False, alpha, beta))
                    b[r][c] = '_'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == '_':
                    b[r][c] = 'O'
                    best = min(best, minimax(b, depth + 1, True, alpha, beta))
                    b[r][c] = '_'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if b[r][c] == '_':
                b[r][c] = 'X'
                move_val = minimax(b, 0, False, -math.inf, math.inf)
                b[r][c] = '_'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (r, c)
    return best_move

def play_game():
    board = [['_'] * 3 for _ in range(3)]
    while True:
        print_board(board)
        if check_winner(board):
            print("Winner:", check_winner(board))
            break
        if all(board[r][c] != '_' for r in range(3) for c in range(3)):
            print("It's a draw!")
            break
        if sum(row.count('_') for row in board) % 2 == 0:
            print("AI's Move:")
            r, c = find_best_move(board)
            board[r][c] = 'X'
        else:
            r, c = map(int, input("Enter row and column (0-2): ").split())
            if board[r][c] == '_':
                board[r][c] = 'O'
            else:
                print("Invalid move! Try again.")

play_game()
