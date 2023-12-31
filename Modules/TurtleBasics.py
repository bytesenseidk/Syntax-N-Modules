import turtle
import colorsys

draw = turtle.Turtle()
draw.speed(0.5)
screen = turtle.Screen()
screen.bgcolor('black')
color_change = 256
pos = 0

for i in range(512):
	color = colorsys.hsv_to_rgb(pos, 1, 1)
	pos = pos + 1 / color_change
	draw.color(color)
	draw.forward(i ** 1.5)
	draw.left(145)

