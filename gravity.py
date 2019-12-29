import pygame
import time
import random
import math

width = 600
height = 400
radius = 50
amount = 2
balls = []
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]



class object:
	def __init__(self, color, rad, xspeed, yspeed):
		self.color = color
		self.xcor = 0
		self.ycor = 0
		self.rad = rad
		self.xspeed = xspeed
		self.yspeed = yspeed

	def move(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor

def position(x,y):
	x = random.randint(radius, width-radius)
	y = random.randint(radius, height-100)
	for ball in balls:
		if math.sqrt((ball.xcor - x)**2 + (ball.ycor - y)**2) <= radius*2:
			x = random.randint(radius, width-radius)
			y = random.randint(radius, height-100)
	return (x,y)


def convert_y(y):
	y -= height
	y *= -1
	return y


for index in range(amount):
	x = y = 0
	cor = position(x,y)
	speedx = random.randint(-10, 10)
	balls.append(object(random.choice(colors), radius, speedx, 0))
	balls[index].move(cor[0],cor[1])


pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity")

running = True
while running:
	win.fill((255,255,255))
	for ball in balls:
		

		for Ball in balls:
			if ball is not Ball:

				if math.sqrt((ball.xcor - Ball.xcor)**2 + (ball.ycor - Ball.ycor)**2) <= radius*2:

					temp = ball.xspeed
					ball.xspeed = Ball.xspeed
					Ball.xspeed = temp

					temp = ball.yspeed
					ball.yspeed = Ball.yspeed
					Ball.yspeed = temp



		ball.yspeed -= 0.1

		if ball.ycor - radius <= 0:
			ball.yspeed *= -1

			if ball.yspeed**2 < 2:
				ball.yspeed = 0
				

		if ball.xcor + radius >= width:
			ball.xspeed *= -1
		elif ball.xcor - radius <= 0:
			ball.xspeed *= -1


		ball.ycor += ball.yspeed
		ball.xcor += ball.xspeed

		pygame.draw.circle(win, ball.color, (int(ball.xcor), int(convert_y(ball.ycor))), ball.rad)
		
	pygame.display.update()
	time.sleep(0.01)