import turtle #1. import modules
import random
import time

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')
#turtle.screensize(1000,100)

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
my_turtles = [leonardo,michelangelo]

#for t in my_turtles:
  # x = random.randrange(1,101)
  # t.forward(x)
  # t.left(180)
  # t.forward(x)
  # t.left(180)

for i in range(10):
  time.sleep(.7)
  for t in my_turtles:
    x = random.randrange(1,11)
    t.forward(x)


# PART B - complete part B here


window.exitonclick()
