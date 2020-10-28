#Name of File:Lab Activity W5 Problem 3
#
#Programmer Name: Jada Cheng
#Date Published: 10/27/20
#
#Description of what the program does: getting the user to create a polygon
#
#Description of know issues: none?

import turtle
t = turtle.Turtle()

side_num = int(input("How many sides? "))
length_num = int(input("What is the length? "))
line_color = input("Color of the line? ")
fill_color = input("What color to fill it in with? ")

color = [line_color]

def polygon(side_num, length_num):
    t.begin_fill()
    for num in range(side_num):
        t.fillcolor(fill_color)
        t.left(360/side_num)
        t.forward(length_num)
    t.end_fill()

for num in range(side_num):
    t.pencolor(color[num%1])
    polygon(side_num,length_num)
    t.left(75)
