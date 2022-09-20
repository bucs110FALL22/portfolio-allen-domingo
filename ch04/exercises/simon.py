import pygame
pygame.init()
screen = pygame.display.set_mode()
red = [255,0,0]
purple = [255,0,255]
blue = [0,0,255]
green = [0,255,0]
black = [0,0,0]


directions = ["up", "down", "left", "right"]
print("Your arrow keys correspond to the following directions:")
for i in directions:
  if i == "up":
   print("up: red")
   screen.fill(red)
  elif i == "down":
    print("down: purple")
    screen.fill(purple)
  pygame.display.flip
  pygame.time.wait(1000)