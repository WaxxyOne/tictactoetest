import tkinter as tk
from tkinter import messagebox


class TicTacToeApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.game_over = False

        self.status_label = tk.Label(
            root,
            text=f"Player {self.current_player}'s turn",
            font=("Segoe UI", 12, "bold"),
            pady=10,
        )
        self.status_label.grid(row=0, column=0, columnspan=3)

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                root,
                text="",
                font=("Segoe UI", 22, "bold"),
                width=5,
                height=2,
                command=lambda idx=i: self.make_move(idx),
            )
            button.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.reset_button = tk.Button(
            root,
            text="New Game",
            font=("Segoe UI", 10),
            command=self.reset_game,
        )
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=(5, 10))

    def make_move(self, index: int) -> None:
        if self.game_over or self.board[index]:
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        winner = self.get_winner()
        if winner:
            self.status_label.config(text=f"Player {winner} wins!")
            self.game_over = True
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            return

        if all(cell for cell in self.board):
            self.status_label.config(text="It's a draw!")
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def get_winner(self) -> str | None:
        win_patterns = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in win_patterns:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.highlight_winner(a, b, c)
                return self.board[a]
        return None

    def highlight_winner(self, a: int, b: int, c: int) -> None:
        for index in (a, b, c):
            self.buttons[index].config(bg="#b1f2b2")

    def reset_game(self) -> None:
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.game_over = False
        self.status_label.config(text=f"Player {self.current_player}'s turn")

        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
