from turtle import *
import turtle as tu


screen=tu.Screen()
screen.bgcolor("white")


tu=tu.Turtle()


tu.penup()
tu.left(90)
tu.fd(200)
tu.pendown()
tu.right(90)


tu.fillcolor("Yellow")
tu.begin_fill()
tu.circle(10,180)
tu.circle(25,110)
tu.left(50)
tu.circle(60,45)
tu.circle(20,170)
tu.right(24)
tu.fd(30)
tu.left(10)
tu.circle(30,110)
tu.fd(20)
tu.left(40)
tu.circle(90,70)
tu.circle(30,150)
tu.right(30)
tu.fd(15)
tu.circle(80,90)
tu.left(15)
tu.fd(45)
tu.right(165)
tu.fd(20)
tu.left(155)
tu.circle(150,80)
tu.left(50)
tu.circle(150,90)
tu.end_fill()


tu.left(150)
tu.circle(-90,70)
tu.left(20)
tu.circle(75,105)
tu.setheading(60)
tu.circle(80,98)
tu.circle(-90,40)

tu.left(180)
tu.circle(90,40)
tu.circle(-80,98)
tu.setheading(-83)

tu.fd(30)
tu.left(90)
tu.fd(25)
tu.left(45)
tu.fillcolor("dark green")
tu.begin_fill()
tu.circle(-80,90)
tu.right(90)
tu.circle(-80,90)
tu.end_fill()
tu.right(135)
tu.fd(60)
tu.left(180)
tu.fd(85)
tu.left(90)
tu.fd(80)

tu.right(90)
tu.right(45)
tu.fillcolor("dark green")
tu.begin_fill()
tu.begin_fill()
tu.circle(80,90)
tu.left(90)
tu.circle(80,90)
tu.end_fill()
tu.left(135)
tu.fd(60)
tu.left(180)
tu.fd(60)
tu.right(90)
tu.circle(200,60)
screen.exitonclick()





