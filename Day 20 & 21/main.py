from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)


#TODO1: Create the snake body
snake = Snake()


#TODO2: Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


#TODO3: Control the snake

#TODO4: Detect collision with food

#TODO5: Create scoreboard

#TODO6: End game (Collision with wall)

#TODO7: End game (Collision with tail)

screen.exitonclick()