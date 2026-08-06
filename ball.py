from turtle import Turtle,Screen
import random
screen=Screen()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0,0)

    def left(self):
        self.setheading(random.randint(110,230))
    def right(self):
        self.setheading(random.randint(290,430))
    def move(self):
        self.forward(20)     
    def change1(self):
        self.setheading(180-self.heading())
    def change2(self):
        self.setheading(360-self.heading())
    
