from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen set up

screen = Screen()
screen_size = 600
boundary = (screen_size / 2) - 5
screen.setup(width=screen_size, height=screen_size)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# Create Snake Body

new_snake = Snake()

# Create food

food = Food()

# Create Scoreboard

scoreboard = Scoreboard()

# Listen to keys

screen.listen()
screen.onkey(fun=new_snake.up, key='Up')
screen.onkey(fun=new_snake.down, key='Down')
screen.onkey(fun=new_snake.left, key='Left')
screen.onkey(fun=new_snake.right, key='Right')

# Move Snake automatically

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    # Detect collision from food

    if new_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        new_snake.extend_snake()

    # Detect Collision with wall

    if new_snake.head.xcor() > boundary \
            or new_snake.head.xcor() < -boundary \
            or new_snake.head.ycor() > boundary \
            or new_snake.head.ycor() < -boundary:
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        new_snake.clear_snake()

    # Detect Collision with tail

    for seg in new_snake.segments[1:]:
        if new_snake.head.distance(seg) < 10:
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            new_snake.clear_snake()









screen.exitonclick()