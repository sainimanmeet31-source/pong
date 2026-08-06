from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
    def display(self,a):
        self.clear()
        self.write(f'{a}',font=('Arial',12,'normal'))
        
        
        
