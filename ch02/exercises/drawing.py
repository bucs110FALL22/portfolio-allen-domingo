import turtle

circle_deg = 360
sides = int(input("What is the number of sides?"))
leng = float(input("What is the length of each side?"))

my_turtle = turtle.Turtle()
my_turtle.shape("classic")
window = turtle.Screen()

colors = ("red","green")

for c in colors:
  my_turtle.color(c)
  for i in [0]*sides:
    my_turtle.left(circle_deg/sides)
    my_turtle.forward(leng)
  my_turtle.up()
  my_turtle.forward(leng*(leng/2))
  my_turtle.down()
                    
window.exitonclick()