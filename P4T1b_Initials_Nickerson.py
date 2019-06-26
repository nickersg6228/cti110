#This program will import the turtle design and write out my initials GN
#June 26, 2019
#CTI-110-P4T1-Initials
#Guadalupe Nickerson


import turtle          
win = turtle.Screen()  
g = turtle.Turtle()
g.pensize(8)           
g.pencolor("purple")     
g.shape("turtle")

#Drawing letter G
g.pendown()
g.left(90)
g.forward(20)
g.left(90)
g.forward(20)
g.back(20)
g.left(90)
g.forward(20)
g.right(90)
g.forward(20)
g.right(45)
g.forward(30)
g.right(45)
g.forward(20)
g.right(45)
g.forward(20)
g.right(45)
g.forward(25)
g.penup()
g.forward(10)

#Drawing letter N
g.pendown()
g.right(90)
g.forward(50)
g.back(50)
g.left(30)
g.forward(60)
g.left(150)
g.forward(53)
g.back(53)
g.right(90)
g.penup()
g.forward(50)
