# A simple Ping Pong game using Python 3 Programming language and the module called turtle
#By Edna Sawe Kite

#Import the required modules
import turtle
import winsound
import flask
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pong.py/')
def pong():
    print('Start Game')

    return 'PLAY'

if __name__ == '__main__':
    app.run(debug=True)

#Create the game screen
windw = turtle.Screen()
windw.title("Ping Pong Game by Edna Sawe")
windw.bgcolor("green")
windw.setup(width=800, height=600)
windw.tracer(0)

#Create the score to count scores
score_right = 0
score_left = 0

#Create the left paddle of the game
paddle_left = turtle.Turtle()
paddle_left.speed(1)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("black")
paddle_left.penup()
paddle_left.goto(-350, 0)

#Create the right paddle of the game
paddle_right = turtle.Turtle()
paddle_right.speed(1)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color("black")
paddle_right.penup()
paddle_right.goto(350, 0)

#Creating the white ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.8

#Creating the pen to record players' scores
pen = turtle.Turtle()
pen.speed(1)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER A: 0 PLAYER B: 0", align="center", font=("Courier", 28, "normal"))

#Creating function to play the game

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


#Creating the keyboard bindings to use when playing the game
windw.listen()
windw.onkeypress(paddle_left_up, "w")
windw.onkeypress(paddle_left_down, "s")
windw.onkeypress(paddle_right_up, "Up")
windw.onkeypress(paddle_right_down, "Down")


#Create the main game looping function
while True:
    windw.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Checking the border on top, bottom, rigt, and left
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 350:
        score_left += 1
        pen.clear()
        pen.write("PLAYER A: {} PLAYER B: {}".format(score_left, score_right), align="center", font=("Courier", 28, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_right += 1
        pen.clear()
        pen.write("PLAYER A: {} PLAYER B: {}".format(score_left, score_right), align="center", font=("Courier", 28, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

        #Paddle and the ball collisions solution\
        if ball.xcor() < -340 and ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        elif ball.xcor() > 340 and ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
