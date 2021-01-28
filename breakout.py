from turtle import *
from time import sleep
import random, keyboard, math

ht()
setup(width=800, height=700)

block_color_row_len = 0
block_Place_X = 0
block_Place_y = 0
blocks = 0
Lives = 3
Alive_blocks_int = 0
Resets = 0
Prev_x = 0
Prev_y = 0
new_x = 0
new_y =0

ball_x = 0

Paddle_dir = 135
paddle_right = 0
paddle_left = 0

block_pos = [(-350,250), (-250,250), (-150,250), (-50,250), (50,250), (150,250), (250,250), (350,250),
             (-350,210), (-250,210), (-150,210), (-50,210), (50,210), (150,210), (250,210), (350,210),
             (-350,170), (-250,170), (-150,170), (-50,170), (50,170), (150,170), (250,170), (350,170),
             (-350,130), (-250,130), (-150,130), (-50,130), (50,130), (150,130), (250,130), (350,130),
             (-350,90), (-250,90), (-150,90), (-50,90), (50,90), (150,90), (250,90), (350,90)]
block_default = [True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True]
block_y = [250, 250, 250, 250, 250, 250, 250, 250,
           210, 210, 210, 210, 210, 210, 210, 210,
           170, 170, 170, 170, 170, 170, 170, 170,
           130, 130, 130, 130, 130, 130, 130, 130,
           90, 90, 90, 90, 90, 90, 90, 90]
block_x = [-350, -250, -150, -50, 50, 150, 250, 350,
           -350, -250, -150, -50, 50, 150, 250, 350,
           -350, -250, -150, -50, 50, 150, 250, 350,
           -350, -250, -150, -50, 50, 150, 250, 350,
           -350, -250, -150, -50, 50, 150, 250, 350]
block_color_row = [8, 8, 8, 8, 8]
block_color = ['red', 'orange', 'yellow', 'green', 'blue']
block_color_cur = []
block_alive = []

blocks = len(block_pos)

def block(Turtle, Color):
    block_Place_X = Turtle.xcor() - 40
    block_Place_y = Turtle.ycor() - 10

    Turtle.goto(block_Place_X, block_Place_y)
    Turtle.color(Color)
    Turtle.begin_fill()
    Turtle.pd()

    Turtle.goto(block_Place_X, block_Place_y + 20)
    Turtle.goto(block_Place_X + 80, block_Place_y + 20)
    Turtle.goto(block_Place_X + 80, block_Place_y)
    Turtle.goto(block_Place_X, block_Place_y)

    Turtle.end_fill()
    Turtle.pu()
    Turtle.goto(block_Place_X + (block_Place_X / 2), block_Place_y + (block_Place_y / 2))

def New(Turtle):
    global block_pos, block, block_color, block_color_row_len, block_color_cur, block_default, block_alive, blocks

    Turtle.clear()

    block_color_row_len = len(block_color_row)
    block_color_cur = []
    block_alive = block_default

    for i in range(block_color_row_len):
        for a in range(block_color_row[i]):
            block_color_cur.append(block_color[i])
    
    for i in range(blocks):
        Turtle.goto(block_pos[i])
        
        block(Turtle, block_color_cur[i])

ts = getscreen()
ts.bgcolor('white')
title('Breakout Game')

block_creator = Turtle()
Paddle = Turtle()
ball = Turtle()

block_creator.color('black')
Paddle.color('green')
ball.color('black')

block_creator.pu()
Paddle.pu()
ball.pu()

block_creator.speed(1000)
Paddle.speed(1000)
ball.speed(1000)

block_creator.goto(0, 0)
Paddle.goto(0, -300)
ball.goto(0, 0)

block_creator.ht()

Paddle.shape("square")
Paddle.shapesize(stretch_wid=1, stretch_len=8, outline=None)
ball.shape("circle")

New(block_creator)

ball.seth(270)

while True:
    prev_x = round(ball.xcor())
    prev_y = round(ball.ycor())
    
    ball.fd(8)

    new_x = round(ball.xcor())
    new_y = round(ball.ycor())
    
    if keyboard.is_pressed('a') or keyboard.is_pressed('left') and not Paddle.xcor() < -350:
        Paddle.bk(8)
    elif keyboard.is_pressed('d') or keyboard.is_pressed('right') and Paddle.xcor() < -340:
        Paddle.fd(8)
    if keyboard.is_pressed('d') or keyboard.is_pressed('right') and not Paddle.xcor() > 350:
        Paddle.fd(8)
    elif keyboard.is_pressed('a') or keyboard.is_pressed('left') and Paddle.xcor() > 340:
        Paddle.bk(8)

    if keyboard.is_pressed('Esc'):
        bye()
        break

    if keyboard.is_pressed('space'):
        ball.goto(random.choice(block_pos))

    if(round(ball.ycor()) <= Paddle.ycor() and round(ball.ycor()) >= Paddle.ycor() - 4):
        paddle_right = round(Paddle.xcor())
        paddle_right += 90

        paddle_left = round(Paddle.xcor())
        paddle_left -= 90

        ball_x = round(ball.xcor())
        
        Paddle_dir = 135
        
        for i in range(paddle_left, paddle_right):

            Paddle_dir -= .5
            
            if(int(round(ball_x)) == int(round(i))):
                ball.seth(Paddle_dir + 0.5)
                break
    if(round(ball.ycor()) >= 80):
        for i in range(blocks):
            for a in range(block_x[i] - 50, block_x[i] + 50):
                if(round(ball.xcor()) == a):
                    for f in range(block_y[i] - 25, block_y[i] + 25):
                        if(round(ball.ycor()) == f):
                            if(block_alive[i] == True):
                                block_alive[i] = False
                                block_creator.goto(block_pos[i])
                                block(block_creator, 'white')
                                ball.sety(ball.ycor() + 0.01)
                                ball.sety(ball.ycor() - 0.01)
                                ball.seth(-ball.heading())

    if(ball.ycor() < -370):
        if(Lives >= 1 and Lives != 0):
            Lives -= 1
            ball.seth(270)
            ball.goto(0, 0)
            Paddle.setx(0)
            for i in range(3):
                ball.color('red')
                sleep(0.2)
                ball.color('black')
                sleep(0.2)
        if(Lives == 0):
            ball.seth(270)
            ball.goto(0, 0)
            Paddle.setx(0)
            ball.color('red')
            sleep(2)
        
    if(Lives <= 0 or Resets > 3):
        bye()
        break

    if(round(ball.ycor()) >= 330):
        ball.seth(-ball.heading())
    if(round(ball.xcor()) >= 400 or round(ball.xcor()) <= -400):
        ball.seth(-ball.heading() + 180)

    Alive_blocks_int = 0
    
    for i in range(blocks):
        if(block_alive[i] == False):
            Alive_blocks_int += 1

    if(Alive_blocks_int == 40):
        Resets += 1
        New(block_creator)
        ball.goto(0, 0)
        ball.seth(270)
        Paddle.setx(0)
        block_alive = block_default