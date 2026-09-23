import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        self.mode = ""
        self.difficulty = ""
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 0

        self.show_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------- MAIN MENU ----------------
    def show_main_menu(self):
        self.clear_window()

        tk.Label(
            self.root,
            text="🎯 NUMBER GUESSING GAME",
            font=("Arial", 22, "bold")
        ).pack(pady=35)

        tk.Label(
            self.root,
            text="Choose Game Mode",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="👤 Single Player",
            font=("Arial", 14),
            width=22,
            command=lambda: self.select_difficulty("Single Player")
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="👥 Double Player",
            font=("Arial", 14),
            width=22,
            command=lambda: self.start_double_player()
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="❌ Exit",
            font=("Arial", 12),
            width=15,
            command=self.root.destroy
        ).pack(pady=25)

    # ---------------- DIFFICULTY ----------------
    def select_difficulty(self, mode):
        self.mode = mode
        self.clear_window()

        tk.Label(
            self.root,
            text="Select Difficulty",
            font=("Arial", 22, "bold")
        ).pack(pady=40)

        tk.Button(
            self.root,
            text="🟢 Easy (1 - 50)",
            font=("Arial", 14),
            width=22,
            command=lambda: self.start_single_player(50, 10)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="🟡 Medium (1 - 100)",
            font=("Arial", 14),
            width=22,
            command=lambda: self.start_single_player(100, 7)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="🔴 Hard (1 - 500)",
            font=("Arial", 14),
            width=22,
            command=lambda: self.start_single_player(500, 10)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="⬅ Back",
            command=self.show_main_menu
        ).pack(pady=25)

    # ---------------- SINGLE PLAYER ----------------
    def start_single_player(self, maximum, attempts):
        self.mode = "Single Player"
        self.secret_number = random.randint(1, maximum)
        self.attempts = 0
        self.max_attempts = attempts

        self.show_game_screen(
            f"Guess a number between 1 and {maximum}"
        )

    # ---------------- DOUBLE PLAYER ----------------
    def start_double_player(self):
        self.mode = "Double Player"
        self.clear_window()

        tk.Label(
            self.root,
            text="👥 DOUBLE PLAYER MODE",
            font=("Arial", 22, "bold")
        ).pack(pady=35)

        tk.Label(
            self.root,
            text="Player 1: Enter a secret number",
            font=("Arial", 14)
        ).pack(pady=10)

        self.secret_entry = tk.Entry(
            self.root,
            font=("Arial", 16),
            width=15,
            show="*"
        )
        self.secret_entry.pack(pady=10)

        tk.Label(
            self.root,
            text="Player 2 will try to guess the number!",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Start Game",
            font=("Arial", 14),
            command=self.set_double_number
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="⬅ Back",
            command=self.show_main_menu
        ).pack(pady=10)

    def set_double_number(self):
        try:
            number = int(self.secret_entry.get())

            if number < 1 or number > 100:
                messagebox.showwarning(
                    "Invalid Number",
                    "Please enter a number between 1 and 100."
                )
                return

            self.secret_number = number
            self.attempts = 0
            self.max_attempts = 10

            messagebox.showinfo(
                "Game Started",
                "Player 1 has set the number!\nNow Player 2 can start guessing."
            )

            self.show_game_screen(
                "Player 2: Guess a number between 1 and 100"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )

    # ---------------- GAME SCREEN ----------------
    def show_game_screen(self, instruction):
        self.clear_window()

        tk.Label(
            self.root,
            text="🎯 GUESS THE NUMBER",
            font=("Arial", 22, "bold")
        ).pack(pady=25)

        tk.Label(
            self.root,
            text=instruction,
            font=("Arial", 13)
        ).pack(pady=10)

        self.guess_entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            width=15
        )
        self.guess_entry.pack(pady=15)

        tk.Button(
            self.root,
            text="🎯 Guess",
            font=("Arial", 14, "bold"),
            width=15,
            command=self.check_guess
        ).pack(pady=10)

        self.result_label = tk.Label(
            self.root,
            text="Good luck! 🍀",
            font=("Arial", 14)
        )
        self.result_label.pack(pady=15)

        self.attempt_label = tk.Label(
            self.root,
            text=f"Attempts: 0 / {self.max_attempts}",
            font=("Arial", 12)
        )
        self.attempt_label.pack(pady=5)

        tk.Button(
            self.root,
            text="🏠 Main Menu",
            command=self.show_main_menu
        ).pack(pady=25)

        self.guess_entry.focus()

    # ---------------- CHECK GUESS ----------------
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())

            self.attempts += 1

            self.attempt_label.config(
                text=f"Attempts: {self.attempts} / {self.max_attempts}"
            )

            if guess == self.secret_number:
                score = max(
                    100 - (self.attempts - 1) * 10,
                    10
                )

                self.result_label.config(
                    text=f"🎉 Correct! Score: {score}",
                    font=("Arial", 16, "bold")
                )

                messagebox.showinfo(
                    "🎉 You Won!",
                    f"Congratulations!\n\n"
                    f"You guessed the number {self.secret_number} "
                    f"in {self.attempts} attempts.\n\n"
                    f"Score: {score}"
                )

                self.end_game()

            elif guess < self.secret_number:
                self.result_label.config(
                    text="⬆ Too Low! Try a higher number."
                )

            else:
                self.result_label.config(
                    text="⬇ Too High! Try a lower number."
                )

            if self.attempts >= self.max_attempts:
                if guess != self.secret_number:
                    messagebox.showinfo(
                        "Game Over",
                        f"❌ Game Over!\n\n"
                        f"The correct number was {self.secret_number}."
                    )
                    self.end_game()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )

    # ---------------- END GAME ----------------
    def end_game(self):
        self.guess_entry.config(state="disabled")

        tk.Button(
            self.root,
            text="🔄 Play Again",
            font=("Arial", 13),
            command=self.show_main_menu
        ).pack(pady=5)


# ---------------- RUN GAME ----------------

root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
