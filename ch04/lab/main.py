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

center = center_x,center_y
radius = x/2
background = (255,0,50)
circle_color = "green"
line_color = "black"
vertical_start =x/2,0
vertical_end = x/2,y
horizontal_start = 0,y/2
horizontal_end = x,y/2

msg = "Choose a color"
font_x = x/3
font_y = y/4
font_pos = font_x,font_y
font = pygame.font.Font(None,20)
font_object = font.render(msg,True,"green")


red_rect = 0,0, center_x, center_y
blue_rect = center_x,0,center_x,center_y

print("Player 1: Choose a color, Player 2 will be the other color.")
i = 0
while i == 0:
  pygame.draw.rect(window,color1,red_rect)
  pygame.draw.rect(window,color2,blue_rect)
  window.blit(font_object,font_pos)
  pygame.display.flip()
  for event in pygame.event.get():
   if event.type == pygame.MOUSEBUTTONDOWN:
     print("mouse down")
     x_pos,y_pos = pygame.mouse.get_pos()
     if y_pos < center_y:
       i += 1
     elif y_pos > center_y:
       print("Please click an actual box")
   pygame.time.wait(20)
    
pygame.time.wait(1000)

if x_pos < center_x:
  print("Player 1 chose red")
  player1 = "Red"
  player2 = "Blue"
elif x_pos >= center_x:
  print("Player 1 chose blue")
  player1 = "Blue"
  player2 = "Red"
  
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

dart_size = 4
player1_dart_color = player1
player2_dart_color = player2
player1_score = 0
player2_score = 0

for d in range(1,11):
 round_number = d
 print("Round",round_number,":")
 print("Player",player1,"shoots!")
 pygame.time.wait(1000)
 dart_x = random.randrange(1,x)
 dart_y = random.randrange(1,y)
 dart_place = dart_x,dart_y
 distance_from_center = math.hypot(center_x-dart_x,center_y-dart_y)
 is_in_circle = distance_from_center <= radius
 if is_in_circle:
   dart_color = player1_dart_color
   player1_score +=1
   print("score!")
 else:
   dart_color = (255,255,0)
   print("miss!")
 pygame.draw.circle(window,dart_color,dart_place,dart_size) 
 pygame.display.flip()
 pygame.time.wait(750)
 print("Player",player2,"shoots!")
 pygame.time.wait(1000)
 dart_x = random.randrange(1,x)
 dart_y = random.randrange(1,y)
 dart_place = dart_x,dart_y
 distance_from_center = math.hypot(center_x-dart_x,center_y-dart_y)
 is_in_circle = distance_from_center <= radius
 if is_in_circle:
   dart_color = player2_dart_color
   player2_score +=1
   print("score!")
 else:
   dart_color = (0,150,0)
   print("miss!")
 pygame.draw.circle(window,dart_color,dart_place,dart_size)
 pygame.display.flip()
 pygame.time.wait(1000)

pygame.time.wait(2000)
print("Score: Player",player1,":",player1_score,"Player",player2,":",player2_score)
if player1_score > player2_score:
  print("Player",player1,"won! You guessed correctly!")
elif player1_score < player2_score:
  print("Player",player2,"won! You didn't guess correctly!")
elif player1_score == player2_score:
  print("It's a tie!")