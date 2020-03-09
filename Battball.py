#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Batball.py
#  
#  Copyright 2020 Rick Bhattacharya <Rick@Serena>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#	Basic python game with basic python code add the provided bounce.wav to add the sound effect otherwise it will give you an error .
#	For MAC devices use  os.system("afplay bounce.wav&")
#	For Windows devices use winsound.Playsound("bounce.wav", winsound.SND_ASYNC) and import winsound
#
#



import turtle
import os

#window enviornment
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Bat 1
bat1 = turtle.Turtle()
bat1.speed(0)
bat1.shape("square")
bat1.color("#F32C01")
bat1.shapesize(stretch_wid=5,stretch_len=1)
bat1.penup()
bat1.goto(-350, 0)

def bat1_up():
    y = bat1.ycor()
    y += 20
    bat1.sety(y)

def bat1_down():
    y = bat1.ycor()
    y -= 20
    bat1.sety(y)

	# Bat 2
bat2 = turtle.Turtle()
bat2.speed(0)
bat2.shape("square")
bat2.color("green")
bat2.shapesize(stretch_wid=5,stretch_len=1)
bat2.penup()
bat2.goto(350, 0)

def bat2_up():
    y = bat2.ycor()
    y += 20
    bat2.sety(y)

def bat2_down():
    y = bat2.ycor()
    y -= 20
    bat2.sety(y)

	# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

	# Net
net = turtle.Turtle()
net.speed(0)
net.shape("square")
net.color("gray")
net.shapesize(stretch_wid=50,stretch_len=1)
net.penup()
net.goto(0, 0)



	#score_board
score_board = turtle.Turtle()
score_board.speed(0)
score_board.shape("square")
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



# Keyboard bindings
wn.listen()
wn.onkeypress(bat1_up, "w")
wn.onkeypress(bat1_down, "s")
wn.onkeypress(bat2_up, "Up")
wn.onkeypress(bat2_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay  bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        score_board.clear()
        score_board.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.color("white")
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        score_board.clear()
        score_board.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.color("white")
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < bat1.ycor() + 50 and ball.ycor() > bat1.ycor() - 50:
        ball.dx *= -1 
        os.system("aplay bounce.wav&")
        ball.color("#F32C01")
    
    elif ball.xcor() > 340 and ball.ycor() < bat2.ycor() + 50 and ball.ycor() > bat2.ycor() - 50:
        ball.dx *= -1
        os.system("aplay bounce.wav&")
        ball.color("green")
