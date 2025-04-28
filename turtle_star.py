
# turtleモジュールを使う
from turtle import Turtle, Screen
import random

list_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def color_choice():
    return random.choice(list_colors)

tim = Turtle()
turtle.colormode(255)
tim.speed(0)
tim.hideturtle()


# スタート地点を調整する
tim.setheading(150)
tim.forward(300)
tim.setheading(0)

# 星を描くには5回線を引く（角度はちょっと特別）
for line in range(5):
    tim.color(color_choice())  # まず色を変える
    tim.forward(100)           # それから前に進む
    tim.right(144)
        
screen = Screen()
# 最後は画面が消えないように待つ（クリック待ちなど）
screen.exitonclick()

