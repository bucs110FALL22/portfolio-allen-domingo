import turtle #1. import modules
import random
import time
import pygame
import math

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

# for i in range(10):
#   time.sleep(.7)
#   for t in my_turtles:
#     x = random.randrange(1,11)
#     t.forward(x)


# PART B - complete part B here
pygame.init()

window = pygame.display.set_mode()

color = "purple"

num_sides = 3
side_length = 20
offset = 20
times = 3
coords = (20,20)

for i in range(num_sides):
  theta = (2.0*math.pi*times/num_sides)
  x = side_length*math.cos(theta)+offset
  y = side_length*math.sin(theta)+offset
  
  coords.append(x)
  coords.append(y)

pygame.draw.polygon(window, color, coords)
window.exitonclick()
