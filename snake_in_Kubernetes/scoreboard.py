from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.score = 0
        self.goto(x=0, y=260)
        self.update_scoreboard() # Typo fixed here
        self.hideturtle()

    def update_scoreboard(self): # Typo fixed here
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=("Times New Roman", 30, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard() # Typo fixed here
