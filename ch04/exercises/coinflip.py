import turtle
import random
distance = 10
angle = 90
x = 250
y = 250
window = turtle.Screen()
window.setup(x,y)
window.bgcolor("lightblue")
t_speed = 0

mr_turt = turtle.Turtle()
mr_turt.color("orange")
mr_turt.shape("turtle")
mr_turt.up()
mr_turt.speed(t_speed)
print(mr_turt.pos())
time.sleep(1)
while True:
  coin_flip = random.randrange(0,2)
  if coin_flip == 0:
    print("heads!")
    mr_turt.left(angle)
    mr_turt.fd(distance)

  elif coin_flip == 1:
    print("tails!")
    mr_turt.right(angle)
    mr_turt.fd(distance)

  turtle_x,turtle_y = mr_turt.pos()
  print(mr_turt.pos())
  if abs(turtle_x) >= (x)/2:
    break
  if abs(turtle_y) >= (y)/2:
    break


window.exitonclick()
  