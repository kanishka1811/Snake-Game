from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0), (-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.createSnake()

    def createSnake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.goto(i)
        self.snake_body.append(t)

    def extend(self):
        print("extend called")
        self.add_segment(self.snake_body[-1].position())
        print('extend executed')

    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1): # we move 3rd segment to 2nd segment position, 2nd segment to 1st segment
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading()!=DOWN: #if it is going DOWN it cannot move UP
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != UP: #if it is going UP it cannot move DOWN
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT: #if it is going RIGHT it cannot move LEFT
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT: #if it is going LEFT it cannot move RIGHT
            self.snake_body[0].setheading(RIGHT)







