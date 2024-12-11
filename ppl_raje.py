import turtle
import random
import tkinter as tk
from turtle import RawTurtle, TurtleScreen

# Create the Tkinter window
root = tk.Tk()
root.title("Cross the Road Game")

# Create a canvas and add it to the window
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Create a TurtleScreen
screen = TurtleScreen(canvas)
screen.bgcolor("lightblue")

# Rest of your turtle setup
screen.tracer(0)

player = RawTurtle(screen)
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -280)
player.setheading(90)

cars = []
car_colors = ["red", "blue", "yellow", "black", "orange"]

for _ in range(10):
    car = RawTurtle(screen)
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2)
    car.color(random.choice(car_colors))
    car.penup()
    car.goto(random.randint(-250, 250), random.randint(-250, 250))
    cars.append(car)

def move_up():
    player.forward(10)

def move_cars():
    for car in cars:
        car.backward(car_speed)
        if car.xcor() < -300:
            car.goto(random.randint(300, 400), random.randint(-250, 250))

def check_collision():
    for car in cars:
        if player.distance(car) < 20:
            return True
    return False

def player_wins():
    return player.ycor() > 280

def next_level():
    global car_speed, level
    player.goto(0, -280)
    level += 1
    car_speed += 5
    level_display.clear()
    level_display.write(f"Level: {level}", align="center", font=("Arial", 16, "bold"))

game_is_on = True
car_speed = 10
level = 1

level_display = RawTurtle(screen)
level_display.hideturtle()
level_display.penup()
level_display.goto(0, 260)
level_display.write(f"Level: {level}", align="center", font=("Arial", 16, "bold"))

# Key binding
screen.listen()
screen.onkey(move_up, "Up")

# Main game loop
def main_loop():
    global game_is_on
    if game_is_on:
        screen.update()
        move_cars()
        if check_collision():
            print("Game Over! You were hit by a car.")
            game_is_on = False
        if player_wins():
            next_level()
    root.after(100, main_loop)

# Start the game loop
main_loop()

# Start the Tkinter event loop
root.mainloop()
