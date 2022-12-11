from turtle import *

#we want to paint a house 

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)  #heigh of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#drawing a window 

penup()
goto(50, 50)
pendown()
color("blue")
left(210)
forward(55)
left(90)
forward(30)
left(90)
forward(55)
right(270)
forward(30)
penup()
goto(180, 50)
pendown()
left(180)
forward(30)
left(270)
forward(55)
right(90)
forward(30)
left(270)
forward(55)

#end of the windows




exitonclick()
