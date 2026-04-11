import random
import tkinter as tk
from tkinter import messagebox

# Global variable to store the player's last move
previous_user_move = None

# Function to handle the AI logic
def ai_move():
    global previous_user_move
    options = ["rock", "paper", "scissors"]
    
    if previous_user_move is None:
        # No previous move, choose randomly
        return random.choice(options)
    else:
        # Predict based on the previous user move
        if previous_user_move == "rock":
            # Player might choose "rock" again, so AI picks "paper"
            return "paper"
        elif previous_user_move == "paper":
            # Player might choose "paper" again, so AI picks "scissors"
            return "scissors"
        else:
            # Player might choose "scissors" again, so AI picks "rock"
            return "rock"

# Function to handle the game logic when the user selects a move
def play(user_choice):
    global previous_user_move
    
    # AI move prediction based on the previous move
    computer_choice = ai_move()

    # Update the previous move
    previous_user_move = user_choice

    # Display the choices in labels
    user_label.config(text=f"Your move: {user_choice}")
    computer_label.config(text=f"Computer's move: {computer_choice}")

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie! Play again!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            result = "You lose! Paper covers rock."
        else:
            result = "You win! Rock smashes scissors."
    elif user_choice == "paper":
        if computer_choice == "scissors":
            result = "You lose! Scissors cut paper."
        else:
            result = "You win! Paper covers rock."
    elif user_choice == "scissors":
        if computer_choice == "rock":
            result = "You lose! Rock smashes scissors."
        else:
            result = "You win! Scissors cut paper."

    # Display the result in the result label
    result_label.config(text=result)

# Function to show an error message for invalid input
def show_error():
    messagebox.showerror("Invalid Input", "Please enter rock, paper, or scissors!")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game with AI")
root.geometry("400x300")

# Labels to display the user's and computer's choices and the result
user_label = tk.Label(root, text="Your move: ", font=("Helvetica", 12))
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer's move: ", font=("Helvetica", 12))
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=20)

# Buttons for the user to choose rock, paper, or scissors
rock_button = tk.Button(root, text="Rock", width=12, command=lambda: play("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=12, command=lambda: play("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=12, command=lambda: play("scissors"))
scissors_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()