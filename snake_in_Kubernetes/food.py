from turtle import Turtle
import random

turtle_colors = ['lawn green','dark green', 'burlywood', 'white', 'red', "saddle brown", "lime green", "yellow", "cyan",
"navy", "olive", 'dark khaki', "olive drab", "dark goldenrod"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(turtle_colors))
        # Ensure x and y coordinates are strict multiples of 20 
        # range(-260, 260) yields multiples: -260, -240 ... 0 ... 240, 260
        random_x = random.randint(-13, 13) * 20
        random_y = random.randint(-13, 13) * 20
        self.goto(random_x, random_y)
