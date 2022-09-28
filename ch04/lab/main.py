import pygame
import random
import math

pygame.init()

window = pygame.display.set_mode((300,300))


x,y = pygame.display.get_window_size()

print(x,y)


center_x = x/2
center_y = y/2

center = center_x,center_y
color1 = "red"
color2 = "blue"
rect1 = 0,0,center_x,y
rect2 = center_x,0,center_x,y

pygame.draw.rect(window,color1,rect1)
pygame.draw.rect(window,color2,rect2)
pygame.display.flip()
for event in pygame.event.get():
 if event.type == pygame.MOUSEBUTTONDOWN:
   print("mouse down")
   x_pos,y_pos = pygame.mouse.get_pos()
   print(x_pos)
 
 
 
  
 
pygame.time.wait(5000)
center = center_x,center_y
radius = x/2
background = (255,0,50)
circle_color = "green"
line_color = "black"
vertical_start = x/2,0
vertical_end = x/2,y
horizontal_start = 0,y/2
horizontal_end = x,y/2
window.fill(background)
pygame.display.flip()
pygame.time.wait(200)

pygame.draw.circle(window,circle_color,center,radius)
pygame.draw.circle(window,line_color,center,radius,width = 2)
pygame.draw.line(window,line_color,vertical_start,vertical_end)
pygame.draw.line(window,line_color,horizontal_start,horizontal_end)

pygame.display.flip()
pygame.time.wait(100)

#Part B

# dart_size = 4
# dart_color = (0,0,255)

# for d in range(10):
#  dart_x = random.randrange(1,x)
#  dart_y = random.randrange(1,y)
#  dart_place = dart_x,dart_y
#  distance_from_center = math.hypot(center_x-dart_x,center_y-dart_y)
#  print(distance_from_center)
  
#  is_in_circle = distance_from_center <= radius
#  if is_in_circle:
#    dart_color = (0,0,255)
#  else:
#   dart_color = (255,255,0)
 
  
#  pygame.draw.circle(window,dart_color,dart_place,dart_size)
#  pygame.display.flip()
#  pygame.time.wait(1000)
# pygame.time.wait(5000)