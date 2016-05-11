Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.home()
>>> turtle.circle(150)
>>> turtle.left(45)
>>> turtle.penup()
>>> turtle.forward(90)
>>> turtle.left(45)
>>> turtle.forward(120)
>>> turtle.pendown()
>>> turtle.circle(30)
>>> turtle.left(90)
>>> turtle.penup()
>>> turtle.forward()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    turtle.forward()
TypeError: forward() missing 1 required positional argument: 'distance'
>>> turtle.forward(75)
>>> turtle.forward(100)
>>> turtle.right(180)
>>> turtle.forward(40)
>>> turtle.circle(30)
>>> 
>>> turtle.right
<function right at 0x0428F030>
>>> turtle.right(90)
>>> turtle.forward(20)
>>> turtle.pendown()
>>> turtle.circle(30)
>>> turtle.penup()
>>> turtle.forward(200)
>>> turtle.right(180)
>>> turtle.right(50)
>>> turtle.forward(13)
>>> turtle.forward(130)
>>> turtle.pendown()
>>> turtle.forward(70)
>>> turtle.fprward(20)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    turtle.fprward(20)
AttributeError: module 'turtle' has no attribute 'fprward'
>>> turtle.forward(20)
>>> turtle.right(170)
>>> turtle.left(20)
>>> turtle.forward(60)
>>> turtle.right(20)
>>> turtle.forward(10)
>>> turtle.right(50)
>>> turtle.forward(30)
>>> turtle.forward(5)
>>> turtle.forward(5)
>>> turtle.forward(5)
>>> turtle.forward(5)
>>> 
