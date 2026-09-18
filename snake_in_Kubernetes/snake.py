from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("arrow")
        self.head.color("spring green")
        # Track the actual direction of the last processed movement frame
        self.current_direction = RIGHT 
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        # Update the direction lock *only* after a successful physical move
        self.current_direction = self.head.heading() 
    
    def up(self):
        if self.current_direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.current_direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.current_direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.current_direction != LEFT:
            self.head.setheading(RIGHT)
    
    def add_segments(self, position):
        snake = Turtle("square")
        snake.color("lime")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    
    def extend(self):
        self.add_segments(self.segments[-1].position())