import tkinter as tk
import random

player_score = 0
computer_score = 0

def play_game(player_choice):
    global player_score, computer_score

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)


    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        player_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    
    label_player_choice.config(text=f"Player: {player_choice.capitalize()}")
    label_computer_choice.config(text=f"Computer: {computer_choice.capitalize()}")
    label_result.config(text=result)
    label_player_score.config(text=f"Player Score: {player_score}")
    label_computer_score.config(text=f"Computer Score: {computer_score}")

window = tk.Tk()
window.title("Rock Paper Scissors")
window.configure(background="black")
window.resizable(False,False)

label_player_choice = tk.Label(window, text="Player: ", font=("Arial", 16), bg="black", fg="white")
label_player_choice.grid(row=0, column=0, padx=10, pady=10)

label_computer_choice = tk.Label(window, text="Computer: ", font=("Arial", 16), bg="black", fg="white")
label_computer_choice.grid(row=0, column=2, padx=10, pady=10)

label_result = tk.Label(window, text="", font=("Arial", 20), bg="black", fg="white")
label_result.grid(row=1, column=1, padx=10, pady=10)

label_player_score = tk.Label(window, text="Player Score: 0", font=("Arial", 16), bg="black", fg="white")
label_player_score.grid(row=2, column=0, padx=10, pady=10)

label_computer_score = tk.Label(window, text="Computer Score: 0", font=("Arial", 16), bg="black", fg="white")
label_computer_score.grid(row=2, column=2, padx=10, pady=10)


button_rock = tk.Button(window, text="Rock", font=("Arial", 16), command=lambda: play_game("rock"), bg="yellow", fg="red")
button_rock.grid(row=3, column=0, padx=10, pady=10)

button_paper = tk.Button(window, text="Paper", font=("Arial", 16), command=lambda: play_game("paper"), bg="yellow", fg="red")
button_paper.grid(row=3, column=1, padx=10, pady=10)

button_scissors = tk.Button(window, text="Scissors", font=("Arial", 16), command=lambda: play_game("scissors"), bg="yellow", fg="red")
button_scissors.grid(row=3, column=2, padx=10, pady=10)


window.mainloop()
