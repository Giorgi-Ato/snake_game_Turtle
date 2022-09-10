from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(x=0, y=260)
        self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.update_data()
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def set_high_score(self):
        with open('data.txt') as f:
            self.high_score = int(f.read())

    def update_data(self):
        with open('data.txt', 'w') as f:
            f.write(str(self.score))
