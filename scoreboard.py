from turtle import Turtle,Screen
FONT=("Courier",24,"normal")
ALIGN="center"
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.write(f"Score : {self.score}",align=ALIGN,font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\nScore is {self.score}",align=ALIGN,font=FONT)
    def increase_speed(self):
        self.score+=1
        self.clear()
        self.update_score()
        
