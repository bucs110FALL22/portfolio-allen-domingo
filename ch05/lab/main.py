import pygame

pygame.init()
display = pygame.display.set_mode()
max_so_far = 0
scale = 20
color = "blue"
go = True
number_start = 101
n = number_start
upper_limit = 20
upper_stop = upper_limit+1
start = 2
stop_value = 1
new_display = pygame.transform.flip(display, False, True)
num = []
font_size = 50
font_color = "green"
max_value = 0


msg_pos = (10,10)

# while abs(n) != stop_value:
#   if n%2 == abs(1):
#     n = 3*n+1
#     print(n)
#     num.append(n)
#   elif n%2 == 0:
#     n = n/2
#     print(n)
#     num.append(n)
number_start = 101
n = number_start
z = start
count = len(num)
print(count)
iters = {}
iters_c = {}
while n !=1:
 for i in range(start,upper_stop):
   print(i)
   if n%2 == abs(1):
     iters[z] = i
     n = 3*n+1
     print(n)
     num.append(n)
     iters_c[scale*z] = -(scale*i)
     if i > max_so_far:
       max_so_far = i
     z +=1
     
   elif n%2 == 0:
     n = n/2
     print(n)
     num.append(n)
   if z ==(upper_stop):
     n = 1
     break


max_value = max_so_far
coords = list(iters_c.items())
pygame.draw.lines(display, color, False, coords)
pygame.display.flip()

max_value = str(max_value)

font_obj = pygame.font.Font(None,font_size)
msg = font_obj.render(max_value,True,font_color)
display.blit(msg,msg_pos)
# display.blit(new_display, (0,0))
pygame.display.flip()
pygame.time.wait(2000)
