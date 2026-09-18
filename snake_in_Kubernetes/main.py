from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title('🐍 SNAKE 🐍')
screen.tracer(0)
WALL = 290

# Global game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# State management variables
game_on = True
is_paused = True
is_game_over = False

def setup_controls():
    """Dynamically binds key listeners to the active Snake object instance"""
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(toggle_pause, 'space')
    screen.onkey(reset_game, 'r')

def toggle_pause():
    """Toggles pause, but blocks it entirely if the score is 3 or higher"""
    global is_paused, is_game_over
    if is_game_over:
        return 
        
    # NEW FEATURE: Increase difficulty by removing pause after 3 points
    if scoreboard.score >= 3:
        # Briefly alert the user that pause is locked out
        scoreboard.clear()
        scoreboard.write("PAUSE DISABLED! KEEP MOVING!", align="center", font=("Courier", 16, "bold"))
        time.sleep(0.5)
        scoreboard.clear()
        scoreboard.update_scoreboard()
        return

    is_paused = not is_paused
    if not is_paused:
        scoreboard.clear()
        scoreboard.update_scoreboard()

def reset_game():
    """Wipes the existing turtle configurations and safely rebuilds the session"""
    global snake, food, scoreboard, game_on, is_paused, is_game_over
    if not is_game_over:
        return 
        
    # 1. Cleanly hide and remove old body assets
    for segment in snake.segments:
        segment.goto(1000, 1000) 
        segment.hideturtle()
    snake.segments.clear()
    
    # 2. Re-instantiate game objects
    snake = Snake()
    food.refresh()
    scoreboard.clear()
    
    # 3. Reset scores and loop controls
    scoreboard.score = 0
    scoreboard.goto(x=0, y=260)
    scoreboard.update_scoreboard()
    
    # 4. Map back to initial standby screen states
    is_paused = True
    is_game_over = False
    game_on = True
    
    # CRITICAL BUG FIX: Re-bind controls to the brand-new snake object instance
    setup_controls()
    
    # Re-draw the start text helper overlay
    scoreboard.goto(0, 0)
    scoreboard.write("Press SPACE to Play/Pause", align="center", font=("Courier", 16, "bold"))
    scoreboard.goto(0, 260)
    screen.update()

# Initial start layout call
scoreboard.goto(0, 0)
scoreboard.write("Press SPACE to Play/Pause", align="center", font=("Courier", 16, "bold"))
scoreboard.goto(0, 260)

# Bind inputs for the first run session
setup_controls()

while True: 
    screen.update()
    time.sleep(0.1)
    
    if not game_on or is_paused:
        continue
        
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL or snake.head.ycor() > WALL or snake.head.ycor() < -WALL:
        game_on = False
        is_game_over = True
        scoreboard.game_over()
        scoreboard.goto(0, -50)
        scoreboard.color("white")
        scoreboard.write("Press 'R' to Replay", align="center", font=("Courier", 14, "normal"))
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            is_game_over = True
            scoreboard.game_over()
            scoreboard.goto(0, -50)
            scoreboard.color("white")
            scoreboard.write("Press 'R' to Replay", align="center", font=("Courier", 14, "normal"))
