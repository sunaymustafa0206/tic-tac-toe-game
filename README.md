# 🎮 Tic-Tac-Toe (Python)

A simple two-player Tic-Tac-Toe game that runs in the terminal, written in Python.

---

## 📋 Requirements

- Python 3.x (no external libraries needed)

---

## 🚀 How to Run

```bash
python tic_tac_toe.py
```

---

## 🕹️ How to Play

1. The game is played by **two players** — Player X and Player O.
2. The board has 9 positions numbered 1 to 9:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

3. On your turn, enter the number of the position where you want to place your mark.
4. Players alternate turns until someone wins or the game ends in a draw.
5. After each game, you can choose to **play again** or quit.

---

## 🏆 Winning Conditions

A player wins by placing three of their marks in a line:

- A horizontal row
- A vertical column
- A diagonal

If all 9 squares are filled with no winner, the game is declared a **draw**.

---

## ✨ Features

- 2-player local multiplayer
- Board displayed after every move
- Win detection for rows, columns, and diagonals
- Draw detection
- Input validation (rejects invalid or already-taken positions)
- Play again option at the end of each game

---

## 📁 File Structure

```
tic_tac_toe.py   # Main game file
README.md        # Project documentation
```

---

## 📝 License

This project is free to use and modify for personal or educational purposes.
