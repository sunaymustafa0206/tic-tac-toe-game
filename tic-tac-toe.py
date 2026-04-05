def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print("  " + " | ".join(row))
        if i < 2:
            print("  ---------")
    print("\n")


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def get_move(board, player):
    while True:
        try:
            move = int(input(f"  Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("  ❌ Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("  ❌ That spot is already taken! Try again.")
                continue
            return row, col
        except ValueError:
            print("  ❌ Invalid input. Please enter a number.")


def play_game():
    print("\n" + "=" * 35)
    print("       🎮  TIC-TAC-TOE  🎮")
    print("=" * 35)
    print("""
  Board positions:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
""")

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        current = 0

        print_board(board)

        while True:
            player = players[current]
            row, col = get_move(board, player)
            board[row][col] = player
            print_board(board)

            if check_winner(board, player):
                print(f"  🏆  Player {player} wins! Congratulations!\n")
                break

            if is_board_full(board):
                print("  🤝  It's a draw! Well played!\n")
                break

            current = 1 - current  # Switch player

        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye! 👋\n")
            break


if __name__ == "__main__":
    play_game()