import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kółko i Krzyżyk")
        self.board = [""] * 9
        self.current_player = "X"

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text="", width=10, height=5, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    game = TicTacToe()
    game.run()
