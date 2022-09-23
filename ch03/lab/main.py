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

for t in my_turtles:
  x = random.randrange(1,101)
  t.forward(x)
  
time.sleep(1)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for i in range(10):
  time.sleep(.7)
  for t in my_turtles:
    x = random.randrange(1,11)
    t.forward(x)

time.sleep(2)
window.clear()
# PART B - complete part B here
pygame.init()

window2 = pygame.display.set_mode()

color = "purple"

def shape_points(num_sides):
  num_sides = num_sides
  side_length = 20
  offset = 100
  
  coords = []

  for i in range(num_sides):
    theta = (2.0*math.pi*i)/num_sides
    x = side_length*math.cos(theta)+offset
    y = side_length*math.sin(theta)+offset
    coords.append([x,y])

  return coords
  

pygame.draw.polygon(window2, 'blue', shape_points(4))
pygame.display.flip()
pygame.time.wait(2000)


window2.fill("black")
pygame.display.flip()

def shape_points(num_sides):
  num_sides = num_sides
  side_length = 20
  offset = 100
  
  coords = []

  for i in range(num_sides):
    theta = (2.0*math.pi*i)/num_sides
    x = side_length*math.cos(theta)+offset
    y = side_length*math.sin(theta)+offset
    coords.append([x,y])

  return coords
  

pygame.draw.polygon(window2, 'blue', shape_points(6))
pygame.display.flip()
pygame.time.wait(2000)
pygame.display.flip()

window2.fill("black")
pygame.display.flip()


def shape_points(num_sides):
  num_sides = num_sides
  side_length = 20
  offset = 100
  #times = 3
  coords = []

  for i in range(num_sides):
    theta = (2.0*math.pi*i)/num_sides
    x = side_length*math.cos(theta)+offset
    y = side_length*math.sin(theta)+offset
    coords.append([x,y])

  return coords
  

pygame.draw.polygon(window2, 'blue', shape_points(9))
pygame.display.flip()
pygame.time.wait(2000)


window2.fill("black")
pygame.display.flip()

def shape_points(num_sides):
  num_sides = num_sides
  side_length = 20
  offset = 100
  #times = 3
  coords = []

  for i in range(num_sides):
    theta = (2.0*math.pi*i)/num_sides
    x = side_length*math.cos(theta)+offset
    y = side_length*math.sin(theta)+offset
    coords.append([x,y])

  return coords
  

pygame.draw.polygon(window2, 'blue', shape_points(360))
pygame.display.flip()
pygame.time.wait(2000)

window2.fill("black")
pygame.display.flip()
