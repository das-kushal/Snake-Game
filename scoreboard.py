from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        # self.high_score
        self.saved()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def saved(self):
        with open('high_score.txt') as f:
            self.high_score = int(f.read())

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over\nScore is {self.score}", align=ALIGN, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_speed(self):
        self.score += 1
        self.update_score()
