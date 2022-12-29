# import colorgram
#
# rgb_color = []
# colors = colorgram.extract("image.jpg", 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

from turtle import Turtle, Screen, colormode
import random
colormode(255)
t = Turtle()
s = Screen()
t.hideturtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.penup()
t.setheading(225)
t.fd(300)
t.setheading(0)
number_of_dots = 100
t.speed(0)
for dot in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.fd(50)
    print(dot)
    if dot % 10 == 0:
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)

s.exitonclick()


