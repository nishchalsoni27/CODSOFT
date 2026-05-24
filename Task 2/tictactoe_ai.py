# ============================================================
#   TASK 2 — TIC-TAC-TOE AI
#   Algorithm : Minimax with Alpha-Beta Pruning
#   Built by  : Nishchal Soni
# ============================================================

import math
import os

# ─────────────────────────────────────────────
#  BOARD HELPERS
# ─────────────────────────────────────────────
def make_board():
    return [" "] * 9          # indices 0-8, row-major


def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n  TIC-TAC-TOE AI  |  Built by Nishchal Soni\n")
    print("  Position guide     Your board")
    print("  ┌───┬───┬───┐     ┌───┬───┬───┐")
    for row in range(3):
        guide = [str(row * 3 + col + 1) for col in range(3)]
        cells = [board[row * 3 + col] for col in range(3)]
        print(f"  │ {guide[0]} │ {guide[1]} │ {guide[2]} │     │ {cells[0]} │ {cells[1]} │ {cells[2]} │")
        if row < 2:
            print("  ├───┼───┼───┤     ├───┼───┼───┤")
    print("  └───┴───┴───┘     └───┴───┴───┘\n")


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]


WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # cols
    (0, 4, 8), (2, 4, 6),              # diagonals
]

def check_winner(board):
    for a, b, c in WIN_COMBOS:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def is_draw(board):
    return " " not in board and check_winner(board) is None


def is_terminal(board):
    return check_winner(board) is not None or is_draw(board)


# ─────────────────────────────────────────────
#  MINIMAX WITH ALPHA-BETA PRUNING
# ─────────────────────────────────────────────
def minimax(board, depth, alpha, beta, is_maximising):
    """
    Recursively evaluate board positions.
    AI  = 'X'  (maximising)
    Human = 'O' (minimising)
    Alpha-Beta pruning cuts off branches that can't affect the result.
    """
    winner = check_winner(board)
    if winner == "X":
        return 10 - depth      # AI wins sooner = better score
    if winner == "O":
        return depth - 10      # Human wins sooner = worse score
    if is_draw(board):
        return 0

    if is_maximising:          # AI's turn — maximise score
        best = -math.inf
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, alpha, beta, False)
            board[move] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:  # Beta cut-off
                break
        return best
    else:                      # Human's turn — minimise score
        best = math.inf
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, alpha, beta, True)
            board[move] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:  # Alpha cut-off
                break
        return best


def best_move(board):
    """Return the index of the AI's best move."""
    best_score = -math.inf
    move = None
    for m in available_moves(board):
        board[m] = "X"
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[m] = " "
        if score > best_score:
            best_score = score
            move = m
    return move


# ─────────────────────────────────────────────
#  GAME LOOP
# ─────────────────────────────────────────────
def get_human_move(board):
    while True:
        try:
            choice = int(input("  Enter position (1-9): "))
            if 1 <= choice <= 9 and board[choice - 1] == " ":
                return choice - 1
            else:
                print("  ⚠  Invalid move. Try again.")
        except ValueError:
            print("  ⚠  Please enter a number between 1 and 9.")


def play_game():
    board = make_board()
    print_board(board)

    # Decide who goes first
    while True:
        first = input("  Do you want to go first? (y/n): ").strip().lower()
        if first in ("y", "n"):
            break
        print("  Please enter 'y' or 'n'.")

    human_turn = first == "y"

    while True:
        print_board(board)

        if human_turn:
            print("  Your turn (O)")
            idx = get_human_move(board)
            board[idx] = "O"
        else:
            print("  AI is thinking... 🤖")
            idx = best_move(board)
            board[idx] = "X"
            print(f"  AI played position {idx + 1}")

        winner = check_winner(board)
        if winner or is_draw(board):
            print_board(board)
            if winner == "O":
                print("  🎉 You win! Congratulations!\n")
            elif winner == "X":
                print("  🤖 AI wins! Better luck next time.\n")
            else:
                print("  🤝 It's a draw! Well played.\n")
            break

        human_turn = not human_turn


def main():
    print("\n" + "=" * 50)
    print("   TIC-TAC-TOE AI — Built by Nishchal Soni")
    print("   Algorithm: Minimax + Alpha-Beta Pruning")
    print("=" * 50)

    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()
