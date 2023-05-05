from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from obstacle import Obstacle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("dark slate gray")
screen.title("My Snake Game")
screen.tracer(0) #to turn off animatiion for each of the segments of the snake body


snake = Snake()
food = Food()
scoreboard = Scoreboard()
obstacle = Obstacle()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on= True

while game_is_on:
    screen.update() #update screen only when all the three segments of snake body have moved
    time.sleep(0.1) #now 0.1 sec delay

    snake.move()

    #detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake_body[0].distance(obstacle) < 15:
        obstacle.refresh()
        scoreboard.decrease_score()

    #detect collision with wall
    if snake.snake_body[0].xcor()>295 or snake.snake_body[0].xcor() <-300 or snake.snake_body[0].ycor() > 300 or snake.snake_body[0].ycor() < -300:
        game_is_on=False
        scoreboard.game_over()



screen.exitonclick()