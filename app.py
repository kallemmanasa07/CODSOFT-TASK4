import tkinter as tk
from tkinter import messagebox
import random

# ---------------- VARIABLES ---------------- #

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

# ---------------- GAME FUNCTION ---------------- #

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(
        text=f"👤 Your Choice: {user_choice}"
    )

    computer_choice_label.config(
        text=f"💻 Computer Choice: {computer_choice}"
    )

    # Determine Winner
    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        user_score += 1

    else:
        result = "😢 Computer Wins!"
        computer_score += 1

    result_label.config(
        text=result
    )

    score_label.config(
        text=f"👤 You: {user_score}     💻 Computer: {computer_score}"
    )


# ---------------- RESET GAME ---------------- #

def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_choice_label.config(
        text="👤 Your Choice: "
    )

    computer_choice_label.config(
        text="💻 Computer Choice: "
    )

    result_label.config(
        text=""
    )

    score_label.config(
        text="👤 You: 0     💻 Computer: 0"
    )


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.configure(bg="#f4f7fb")

# Full Screen
root.state("zoomed")

# ESC to exit fullscreen
root.bind(
    "<Escape>",
    lambda e: root.state("normal")
)

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="✊ ✋ ✌ Rock Paper Scissors",
    font=("Arial", 28, "bold"),
    bg="#f4f7fb",
    fg="#1e3a8a"
)
title.pack(pady=20)

# ---------------- INSTRUCTIONS ---------------- #

instructions = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors to play against the Computer",
    font=("Arial", 14),
    bg="#f4f7fb"
)
instructions.pack(pady=10)

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(
    root,
    bg="#f4f7fb"
)
button_frame.pack(pady=30)

rock_btn = tk.Button(
    button_frame,
    text="✊ Rock",
    font=("Arial", 14, "bold"),
    bg="#2563eb",
    fg="white",
    width=15,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(
    button_frame,
    text="✋ Paper",
    font=("Arial", 14, "bold"),
    bg="#16a34a",
    fg="white",
    width=15,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = tk.Button(
    button_frame,
    text="✌ Scissors",
    font=("Arial", 14, "bold"),
    bg="#dc2626",
    fg="white",
    width=15,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=15)

# ---------------- CHOICES ---------------- #

user_choice_label = tk.Label(
    root,
    text="👤 Your Choice:",
    font=("Arial", 16, "bold"),
    bg="#f4f7fb"
)
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    root,
    text="💻 Computer Choice:",
    font=("Arial", 16, "bold"),
    bg="#f4f7fb"
)
computer_choice_label.pack(pady=10)

# ---------------- RESULT ---------------- #

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 22, "bold"),
    bg="#f4f7fb",
    fg="#7c3aed"
)
result_label.pack(pady=20)

# ---------------- SCORE ---------------- #

score_label = tk.Label(
    root,
    text="👤 You: 0     💻 Computer: 0",
    font=("Arial", 18, "bold"),
    bg="#f4f7fb",
    fg="#0f172a"
)
score_label.pack(pady=20)

# ---------------- RESET BUTTON ---------------- #

reset_btn = tk.Button(
    root,
    text="🔄 Play Again / Reset",
    font=("Arial", 14, "bold"),
    bg="#f59e0b",
    fg="white",
    width=20,
    command=reset_game
)
reset_btn.pack(pady=20)

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="Rock beats Scissors • Scissors beats Paper • Paper beats Rock",
    font=("Arial", 12, "italic"),
    bg="#f4f7fb",
    fg="gray"
)
footer.pack(side="bottom", pady=15)

root.mainloop()