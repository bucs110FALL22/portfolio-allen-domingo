import turtle
window = turtle.Screen()
t_color = "green"
turt = turtle.Turtle()
turt.color(t_color)
def drawEqshape (num_sides = 0,length = 0):

  angle = 360/num_sides
  for i in range(num_sides):
    turt.fd(length)
    turt.left(angle)
    

sides = int(input("How many sides would you like?"))
side_length = float(input("How long would you like each side to be"))
drawEqshape(sides,side_length) 
window.exitonclick()