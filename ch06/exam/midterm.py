import turtle
import math
import random
def calculate_diameter(melon_sides,melon_length):
  PI = math.pi
  '''
  Calculates diameter of the melon
  args:
  melon_sides = (int)number of sides on the watermelon
  melon_length=(float)length of each side of the watermelon
  return: circumfrence of the watermelon
  '''
  half_circ = melon_sides*melon_length
  diam = (2*half_circ/PI)
  return diam
def turtle_start(dTurtle,window):
  '''
  Initializes turtle to create the drawing
  args:
  dTurtle = Turtle object
  window = Turtle Screen
  no return
  '''
  origin = (0,0)
  w_width = 1000
  w_height = 1000
  window.screensize(w_width,w_height) 
  dTurtle.goto(origin)
def watermelon(dTurtle,border_width = 0,num_sides=0,num_length=0):
  '''
  Has turtle draw the 'watermelon'
  args:
  dTurtle = turtle object
  border_width = (float) thickness of turtle line/thickness of watermelon skin
  num_sides = (int)number of sides for the watermelon shape
  num_length = (float) length of each side of the watermelon shape
  no return
  '''
  out_color = "green"
  in_color = "red"
  right_angle = 90
  circle_angle = 180/num_sides
  dTurtle.width(border_width)
  dTurtle.speed(0)
  dTurtle.color(out_color)
  dTurtle.right(right_angle)
  dTurtle.fillcolor(in_color)
  dTurtle.begin_fill()
  for t in range(num_sides):
    dTurtle.fd(num_length)
    dTurtle.left(circle_angle)
  dTurtle.end_fill()
  dTurtle.up()
def eyes(dTurtle,diameter=0,eye_shape=0,side_length=0,num_eyes=0):
  '''
  responsible for drawing and placing the eyes above the melon
  args:
  dTurtle = turtle object
  diameter = (float) diameter of the watermelon
  eye_shape = (int)number of sides for the shape of the eye
  num_eyes = (int)number of eyes desired
  '''
  eye_color = "black"
  fill_color = "green"
  dTurtle.color(eye_color)
  eye_height = 40
  start = 1
  eye_range = num_eyes+1
  west = 180
  dTurtle.fillcolor(fill_color)
  def draw_eye():
    '''
    draws a single eye in a shape of the number of sides given
    '''
    dTurtle.down()
    dTurtle.begin_fill()
    for e in range(eye_shape):
      dTurtle.fd(side_length)
      dTurtle.right(360/eye_shape)
    dTurtle.up()
    dTurtle.end_fill()
  for i in range(start, eye_range):
    dTurtle.setheading(west)
    eye_x = ((i*diameter)/(eye_range))
    dTurtle.goto(eye_x,eye_height)
    draw_eye()
def seed(dTurtle):
  '''
  Draws a single seed 
  Args:
  dTurtle = turtle object
  no return
  '''
  seed_length = 4
  
  dTurtle.down()
  dTurtle.fd(seed_length)
  dTurtle.up()
def seed_maker(dTurtle,mel_diameter=0,num_seeds=0):
  '''
  Draws the seeds in random places
  Args:
  dTurtle = turtle object
  mel_diameter = (float)diameter of the watermelon
  num_seeds = (int)desired number of seeds in the watermelon
  no return
  
  '''
  seed_thickness = 3
  seed_color = "black"
  north = 90
  radius = mel_diameter/2
  bound1 = int(mel_diameter*1/8)
  bound2 = int(mel_diameter*7/8)
  bound_y1 = 15
  angle_start = 0
  angle_stop = 360
  seed_border = int((mel_diameter/16))
  dTurtle.color(seed_color)
  dTurtle.width(seed_thickness)
  dTurtle.setheading(north)
  for n in range(num_seeds):
    seed_angle = random.randrange(angle_start,angle_stop)
    seed_x = int(random.randrange(bound1,bound2))   
    if seed_x <= radius:
      seed_y = random.randrange(bound_y1,int(seed_x-seed_border))
    else:
      seed_y = random.randrange(bound_y1,int(mel_diameter-(seed_x-seed_border)))
    dTurtle.goto(seed_x,-(seed_y))
    dTurtle.right(seed_angle)
    dTurtle.down()
    seed(dTurtle)
    dTurtle.up()
def main():
  PI = math.pi
  sides = 400
  length = 1
  eye_sides = 30
  eye_s_length = 6
  number_eyes = 2
  
  seed_num = 12
  win = turtle.Screen()
  myrtle = turtle.Turtle()
  border = 10
  melon_diameter = calculate_diameter(sides,length)
  turtle_start(myrtle,win)
  watermelon(myrtle,border,sides,length)
  eyes(myrtle,melon_diameter,eye_sides,eye_s_length,number_eyes)
  seed_maker(myrtle,melon_diameter,seed_num)
  win.exitonclick()
main()
