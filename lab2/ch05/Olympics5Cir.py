#Olympics 5环：蓝、黑，红
#Olympics 5环：黄、绿
#blue : (-110,-25) ;  black : (0,-25) ; red : (110,-25) ; yellow : (-55,-75) ; green : (55,-75)
#半径：45像素，画笔宽度：5像素

import turtle

turtle.pensize(5)
turtle.color("blue")
turtle.penup()
turtle.goto(-110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)
