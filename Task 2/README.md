# 🎮 Tic-Tac-Toe AI — Task 2

**Built by:** Nishchal Soni  
**Algorithm:** Minimax with Alpha-Beta Pruning  
**Language:** Python 3 (no external dependencies)

---

## 📌 Overview

An unbeatable AI agent that plays Tic-Tac-Toe against a human player in the terminal.  
The AI uses the **Minimax algorithm** — a classic game-theory search — enhanced with  
**Alpha-Beta Pruning** to cut off branches that cannot affect the final decision, making  
it fast even while evaluating every possible game state.

---

## 🧠 How It Works

```
Human (O)  vs  AI (X)
```

| Concept | Description |
|---|---|
| **Minimax** | Recursively explores all possible moves, assigning scores: AI win = +10, Human win = -10, Draw = 0 |
| **Alpha (α)** | Best score the maximiser (AI) can guarantee so far |
| **Beta (β)** | Best score the minimiser (Human) can guarantee so far |
| **Pruning** | When β ≤ α, remaining branches are skipped — they can't change the outcome |
| **Depth penalty** | Winning sooner scores higher (`10 - depth`), so AI always picks the quickest win |

The AI is **mathematically unbeatable** — at best, a perfect human player achieves a draw.

---

## 🚀 How to Run

### Requirements
- Python 3.7 or higher
- No external libraries needed

### Run the game
```bash
python tictactoe_ai.py
```

---

## 🕹️ How to Play

1. Run the script — a welcome screen appears
2. Choose whether you want to go **first (y)** or **second (n)**
3. The board is shown with a **position guide** (1–9):

```
  Position guide     Your board
  ┌───┬───┬───┐     ┌───┬───┬───┐
  │ 1 │ 2 │ 3 │     │   │   │   │
  ├───┼───┼───┤     ├───┼───┼───┤
  │ 4 │ 5 │ 6 │     │   │   │   │
  ├───┼───┼───┤     ├───┼───┼───┤
  │ 7 │ 8 │ 9 │     │   │   │   │
  └───┴───┴───┘     └───┴───┴───┘
```

4. Enter a number (**1–9**) to place your **O** on that position
5. The AI instantly responds with its best move
6. The game ends with a **win**, **loss**, or **draw** message
7. You can **play again** or quit

---

## 📂 File Structure

```
tictactoe_ai.py        ← Single-file solution, no dependencies
README_tictactoe.md    ← This file
```

---

## 🔍 Code Structure

| Function | Purpose |
|---|---|
| `make_board()` | Creates a fresh 9-cell board |
| `print_board()` | Renders the board + position guide in the terminal |
| `check_winner()` | Checks all 8 win combinations |
| `minimax()` | Core recursive AI algorithm with α-β pruning |
| `best_move()` | Calls minimax for each move and picks the highest-scoring one |
| `get_human_move()` | Validates and reads the human's input |
| `play_game()` | Main game loop |

---

## 💡 Learning Outcomes

- **Game theory** — zero-sum games, optimal strategies
- **Search algorithms** — depth-first tree search
- **Alpha-Beta Pruning** — reduces nodes from O(b^d) to O(b^(d/2))
- **Recursion** — building and unwinding game trees

---

## 📝 Example Session

```
  TIC-TAC-TOE AI  |  Built by Nishchal Soni

  Do you want to go first? (y/n): y

  Your turn (O)
  Enter position (1-9): 5

  AI is thinking... 🤖
  AI played position 1

  ...

  🤝 It's a draw! Well played.

  Play again? (y/n): n
  Thanks for playing! Goodbye 👋
```

---

*Task 2 — CODSOFT AI Internship | Nishchal Soni*
