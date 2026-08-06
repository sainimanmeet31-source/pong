#you were missing the part where the ball had to hit the face of the pad and not the centre only
import turtle
from ball import Ball
from Score import score
from Saddle import saddle
from line import mid_line
import time
screen=turtle.Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
m=mid_line()
m.draw()
screen.tracer(0)
sc1=0
sc2=0
s1=score()
s2=score()
s1.goto(-50,200)
s1.write(f'{sc1}',font=('Arial',12,'normal'))
s2.goto(50,200)
s2.write(f'{sc2}',font=('Arial',12,'normal'))


while sc1!=5 or sc2!=5:
    b1=saddle()
    b1.goto(-220,0)
    b2=saddle()
    b2.goto(220,0)
    ball=Ball()
    screen.update()
    screen.listen()
    screen.onkey(b1.move1,'w')
    screen.onkey(b1.move2,'s')
    screen.onkey(b2.move1,'Up')
    screen.onkey(b2.move2,'Down')
    game_is_on=True
    if sc1==sc2:
        ball.left()
    elif sc1>sc2:
        if sc1==5:
            s1.goto(-50,50)
            ball.clear()
            s1.write('game over',font=('Arial',18,'normal'))
            break
        else:
            ball.right()
    elif sc1<sc2:
        if sc2==5:
            s2.goto(-50,50)
            ball.clear()
            s2.write('game over',font=('Arial',18,'normal'))
            break
        else:
            ball.left()
    while game_is_on==True:
        ball.move()
        screen.update()
        time.sleep(0.1)
        if ball.xcor()>300:
            sc1=sc1+1
            s1.display(sc1)
            ball.reset()
            b1.reset()
            b2.reset()
            screen.update()
            game_is_on=False
        elif ball.xcor()<-300:
            sc2=sc2+1
            s2.display(sc2)
            ball.reset()
            b1.reset()
            b2.reset()
            screen.update()
            game_is_on=False
        elif ball.ycor()>=270 or ball.ycor()<=-280:
            ball.change2()
            screen.update()
        elif (ball.xcor() < -200 and abs(ball.ycor() - b1.ycor()) < 50):
            ball.change1()
        elif (ball.xcor() > 200 and abs(ball.ycor() - b2.ycor()) < 50):
            ball.change1()
 

screen.exitonclick()

