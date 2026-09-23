import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.mode = "Easy"
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 10
        self.score = 0
        self.player_mode = "Single Player"

        self.create_home_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------- HOME SCREEN ----------------

    def create_home_screen(self):
        self.clear_screen()

        title = tk.Label(
            self.root,
            text="🎯 NUMBER GUESSING GAME",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        subtitle = tk.Label(
            self.root,
            text="Guess the hidden number!",
            font=("Arial", 14)
        )
        subtitle.pack(pady=10)

        tk.Label(
            self.root,
            text="Select Difficulty",
            font=("Arial", 15, "bold")
        ).pack(pady=15)

        self.difficulty = tk.StringVar(value="Easy")

        for level in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(
                self.root,
                text=level,
                variable=self.difficulty,
                value=level,
                font=("Arial", 13)
            ).pack()

        tk.Label(
            self.root,
            text="Select Game Mode",
            font=("Arial", 15, "bold")
        ).pack(pady=15)

        self.game_mode = tk.StringVar(value="Single Player")

        tk.Radiobutton(
            self.root,
            text="👤 Single Player",
            variable=self.game_mode,
            value="Single Player",
            font=("Arial", 13)
        ).pack()

        tk.Radiobutton(
            self.root,
            text="👥 2 Player",
            variable=self.game_mode,
            value="2 Player",
            font=("Arial", 13)
        ).pack()

        tk.Button(
            self.root,
            text="🚀 START GAME",
            font=("Arial", 15, "bold"),
            command=self.start_game,
            width=20
        ).pack(pady=30)

        tk.Button(
            self.root,
            text="❌ Exit",
            font=("Arial", 12),
            command=self.root.destroy,
            width=12
        ).pack()

    # ---------------- START GAME ----------------

    def start_game(self):
        self.mode = self.difficulty.get()
        self.player_mode = self.game_mode.get()

        if self.mode == "Easy":
            self.max_number = 50
            self.max_attempts = 10

        elif self.mode == "Medium":
            self.max_number = 100
            self.max_attempts = 8

        else:
            self.max_number = 500
            self.max_attempts = 7

        if self.player_mode == "Single Player":
            self.secret_number = random.randint(1, self.max_number)

        else:
            self.two_player_setup()

    # ---------------- 2 PLAYER SETUP ----------------

    def two_player_setup(self):
        self.clear_screen()

        tk.Label(
            self.root,
            text="👥 2 PLAYER MODE",
            font=("Arial", 24, "bold")
        ).pack(pady=30)

        tk.Label(
            self.root,
            text=f"Player 1: Enter a number between 1 and {self.max_number}",
            font=("Arial", 13)
        ).pack(pady=20)

        self.player1_entry = tk.Entry(
            self.root,
            font=("Arial", 16),
            width=15,
            show="*"
        )
        self.player1_entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Set Number",
            font=("Arial", 13, "bold"),
            command=self.set_player_number
        ).pack(pady=20)

    def set_player_number(self):
        try:
            number = int(self.player1_entry.get())

            if number < 1 or number > self.max_number:
                messagebox.showerror(
                    "Invalid Number",
                    f"Enter a number between 1 and {self.max_number}."
                )
                return

            self.secret_number = number
            self.start_game_screen()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )

    # ---------------- GAME SCREEN ----------------

    def start_game_screen(self):
        self.clear_screen()

        self.attempts = 0

        if self.player_mode == "Single Player":
            self.secret_number = random.randint(1, self.max_number)

        title = tk.Label(
            self.root,
            text="🎯 GUESS THE NUMBER",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=25)

        tk.Label(
            self.root,
            text=f"Difficulty: {self.mode}",
            font=("Arial", 13)
        ).pack()

        tk.Label(
            self.root,
            text=f"Guess a number from 1 to {self.max_number}",
            font=("Arial", 14)
        ).pack(pady=15)

        self.attempt_label = tk.Label(
            self.root,
            text=f"Attempts: 0 / {self.max_attempts}",
            font=("Arial", 13, "bold")
        )
        self.attempt_label.pack(pady=10)

        self.guess_entry = tk.Entry(
            self.root,
            font=("Arial", 20),
            width=12,
            justify="center"
        )
        self.guess_entry.pack(pady=15)

        self.guess_entry.focus()

        tk.Button(
            self.root,
            text="🎯 GUESS",
            font=("Arial", 14, "bold"),
            command=self.check_guess,
            width=15
        ).pack(pady=10)

        self.hint_label = tk.Label(
            self.root,
            text="💡 Enter your guess!",
            font=("Arial", 13),
            wraplength=400
        )
        self.hint_label.pack(pady=20)

        self.score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=("Arial", 13, "bold")
        )
        self.score_label.pack(pady=10)

        tk.Button(
            self.root,
            text="🏠 Main Menu",
            command=self.create_home_screen
        ).pack(pady=15)

    # ---------------- CHECK GUESS ----------------

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a number!"
            )
            return

        if guess < 1 or guess > self.max_number:
            messagebox.showwarning(
                "Out of Range",
                f"Enter a number between 1 and {self.max_number}."
            )
            return

        self.attempts += 1

        self.attempt_label.config(
            text=f"Attempts: {self.attempts} / {self.max_attempts}"
        )

        if guess == self.secret_number:

            points = max(
                10,
                (self.max_attempts - self.attempts + 1) * 10
            )

            self.score += points

            self.score_label.config(
                text=f"Score: {self.score}"
            )

            messagebox.showinfo(
                "🎉 Congratulations!",
                f"You guessed the number!\n\n"
                f"Number: {self.secret_number}\n"
                f"Attempts: {self.attempts}\n"
                f"Points: +{points}"
            )

            self.play_again()

        elif guess < self.secret_number:

            self.hint_label.config(
                text="⬆️ Too Low! Try a HIGHER number."
            )

        else:

            self.hint_label.config(
                text="⬇️ Too High! Try a LOWER number."
            )

        if self.attempts >= self.max_attempts:
            if guess != self.secret_number:

                messagebox.showinfo(
                    "Game Over 😢",
                    f"You ran out of attempts!\n\n"
                    f"The number was {self.secret_number}."
                )

                self.play_again()

        self.guess_entry.delete(0, tk.END)

    # ---------------- PLAY AGAIN ----------------

    def play_again(self):
        answer = messagebox.askyesno(
            "Play Again?",
            "Do you want to play another round?"
        )

        if answer:
            self.start_game()

        else:
            self.create_home_screen()


# ---------------- MAIN PROGRAM ----------------

root = tk.Tk()

game = NumberGuessingGame(root)

root.mainloop()
