from turtle import Turtle
ALIGNMENT = "center"
FONT=("Courier", 16, "normal")

def get_highscore():
    with open("data.txt") as file:
        highscore=file.read()
        return highscore

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=int(get_highscore())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score ={self.score} High Score ={self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()

