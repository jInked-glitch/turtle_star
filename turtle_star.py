import turtle
import random

from PIL import Image
import colorgram

from turtle import Turtle, Screen



img = Image.open("image-sample.jpg")

num_colors = 100
colors = colorgram.extract("image-sample.jpg", num_colors)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

def color_choice():
    return random.choice(rgb_colors)
# print(rgb_colors)

tim = Turtle()
turtle.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()

# スタート地点を調整する
tim.setheading(150)
tim.forward(300)
tim.setheading(0)

for row in range(10):
    for col in range(10):
        tim.dot(20, color_choice())
        if col != 9:
            tim.forward(50)
        # 行が終わったら下に移動してスタート位置に戻る
    tim.setheading(270)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(450)
    tim.setheading(0)  # また右向きに戻す

    # # 1行描き終わったら下に移動
    # tim.setheading(270)  # 下向き
    # tim.forward(50)
    # tim.setheading(180)  # 左向き
    # for col in range(10):
    #     tim.dot(20, color_choice())
    #     if col != 9:
    #         tim.forward(50)
    # tim.setheading(270)  # 下向き
    # tim.forward(50)
    # tim.setheading(0)  # 右向きにリセット
