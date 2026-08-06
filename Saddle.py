from turtle import Turtle

class saddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.setheading(90)
    def move1(self):
        self.setheading(90)
        self.forward(30)
    def move2(self):
        self.setheading(270)
        self.forward(30)
        
