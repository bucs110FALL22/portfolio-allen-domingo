import turtle
import random

window = turtle.Screen()
window.bgcolor("lightblue")
mr_turt = turtle.Turtle()
mr_turt.color("orange")

while True:
  coin_flip = random.randrange(0,2)
  if coin_flip == 0:
    print("heads!")
    