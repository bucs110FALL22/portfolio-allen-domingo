import pygame

pygame.init()
width = 400
height=380
display = pygame.display.set_mode(size=(width,height))



new_display = pygame.transform.flip(display, False, True)
num = []
font_size = 50
font_color = "green"
max_value = 0

msg_pos = (10,10)
max_so_far = 0
scale = 15
color = "blue"
go = True
number_start = 101
x = number_start
upper_limit = 20
upper_stop = upper_limit+1
start = 2
z = start
stop_value = 1


coords = []
iters = {}
iters_c = {}
def sequence(n):
 count=0
 while True:
   if n==1:
     break
  # print(i)
   if n%2 == abs(1):
     n = 3*n+1
    # print(n)
     num.append(n)
     
     count +=1
   
   elif n%2 == 0:
     n = n/2
     # print(n)
     num.append(n)
     count +=1
 # print(count)
 return count

for l in range(start,upper_stop):
  count = sequence(l)
  iters[l] = count
  iters_c[l*scale] = height-count*scale
  coords = list(iters_c.items())

  if count > max_so_far:
    max_so_far = count
    max_value = str(max_so_far)
    display.blit(new_display, (0,0))
    font_obj = pygame.font.Font(None,font_size)
    msg = font_obj.render("the max value is " +max_value,True,font_color)
    display.blit(msg,msg_pos)

    pygame.display.flip()
   
  if l > start+1:
   pygame.draw.lines(display, color, False, coords)
   pygame.display.flip()

   

  pygame.time.wait(500)
max_value = max_so_far 
# print("num:",num)
print("iters:",iters)


pygame.time.wait(2500)
