from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
root = Tk()
root.title("ROCK-PAPER-SCISSOR GAME")
root.geometry("1000x700")
root.resizable(False, False)
bg = Image.open("rock-paper-scissor.jpg").resize((1000, 700))
bgm = ImageTk.PhotoImage(bg)
canvas = Canvas(root, width=1000, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bgm, anchor="nw")
user_score = 0
computer_score = 0
def play(user):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissor"]
    computer = random.choice(choices)
    if user == computer:
        result_text = "It's a Draw!"
    elif (user == "Rock" and computer == "Scissor") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissor" and computer == "Paper"):
        result_text = "You Win!"
        user_score += 1
    else:
        result_text = "Computer Wins!"
        computer_score += 1
    result.config(text=f"You chose: {user}\nComputer chose: {computer}\n\n{result_text}")
    score.config(text=f"User: {user_score}     Computer: {computer_score}")
def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result.config(text="Play to see your result")
    score.config(text="User: 0     Computer: 0")
title = Label(root, text="Rock Paper Scissors", font=("Arial Black", 40), bg="#87CEEB", fg="black")
canvas.create_window(500, 50, window=title)
instruction = Label(root, text="Choose your move", font=("Arial", 24), bg="lightblue")
canvas.create_window(500, 120, window=instruction)
rock = Button(root, text="🪨 Rock", font=("Arial", 20), bg="#FFB6C1", width=10, command=lambda: play("Rock"))
paper = Button(root, text="📄 Paper", font=("Arial", 20), bg="#FFB6C1", width=10, command=lambda: play("Paper"))
scissor = Button(root, text="✂ Scissor", font=("Arial", 20), bg="#FFB6C1", width=10, command=lambda: play("Scissor"))
canvas.create_window(350, 190, window=rock)
canvas.create_window(500, 190, window=paper)
canvas.create_window(650, 190, window=scissor)
result = Label(root, text="Play to see your result", font=("Arial", 18), bg="#FAFAD2", width=60, height=4, bd=2, relief="groove")
canvas.create_window(500, 300, window=result)
score = Label(root, text="User: 0     Computer: 0", font=("Arial", 18), bg="#E6E6FA", width=30, bd=2, relief="groove")
canvas.create_window(500, 400, window=score)
reset = Button(root, text="🔄 Reset", font=("Arial", 16), bg="#ADD8E6", command=reset)
canvas.create_window(500, 470, window=reset)
root.mainloop()