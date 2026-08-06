from turtle import Turtle

class mid_line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        self.speed('fastest')
    def draw(self):
        while self.ycor()!=300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
