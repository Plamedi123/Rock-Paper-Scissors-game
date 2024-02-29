import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Rock Paper Scissors")
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")

# Player choices
choices = ["Rock", "Paper", "Scissors"]

# Function to draw hand shape
def draw_hand(choice):
    turtle.clear()  # Clear the previous drawing
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.speed(3)

    if choice == "Rock":
        turtle.shape("circle")
        turtle.shapesize(3)
    elif choice == "Paper":
        turtle.shape("square")
        turtle.shapesize(3, 2)
    else:
        turtle.shape("triangle")
        turtle.shapesize(3)

# Function to draw computer's choice
def draw_computer_hand(choice):
    turtle.penup()
    turtle.goto(150, -50)
    turtle.pendown()
    turtle.speed(3)

    if choice == "Rock":
        turtle.shape("circle")
        turtle.shapesize(3)
    elif choice == "Paper":
        turtle.shape("square")
        turtle.shapesize(3, 2)
    else:
        turtle.shape("triangle")
        turtle.shapesize(3)

# Function to show result
def show_result(player_choice, computer_choice):
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.color("black")
    turtle.write(f"Player: {player_choice}   Computer: {computer_choice}", align="center", font=("Arial", 16, "normal"))

# Function to play the game
def play_game():
    player_choice = screen.textinput("Rock, Paper, Scissors", "Enter your choice (Rock, Paper, Scissors): ").capitalize()
    computer_choice = random.choice(choices)

    draw_hand(player_choice)
    draw_computer_hand(computer_choice)
    show_result(player_choice, computer_choice)

# Main game loop
while True:
    play_game()
    turtle.clear()  # Clear the screen for the next round

    play_again = screen.textinput("Play Again?", "Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

screen.mainloop()
