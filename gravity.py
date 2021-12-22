import pygame
import time
import random
import math


width = 600
height = 400
radius = 100
amount = 2
balls = []
colors = [(27, 38, 44), (15, 76, 117), (50, 130, 184)]



class object:
	def __init__(self, color, radius, xspeed, yspeed):
		self.color = color
		self.xcor = 0
		self.ycor = 0
		self.radius = radius
		self.xspeed = xspeed
		self.yspeed = yspeed

	def move(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor
	
	def update(self):
		self.yspeed -= 0.1

		if self.ycor - self.radius <= 0:
			self.yspeed = abs(self.yspeed)

			if self.yspeed**2 < 2:
				self.yspeed = 0
				
		if self.xcor + radius >= width:
				self.xspeed = -abs(self.xspeed)
		
		if self.xcor - self.radius <= 0:
			self.xspeed = abs(self.xspeed)

		self.move(self.xcor + self.xspeed, self.ycor + self.yspeed)		

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.xcor, convert_y(self.ycor)), self.radius)
	
	def collidesWith(self, ball):
		return ball is not self and math.sqrt((ball.xcor - self.xcor)**2 + (ball.ycor - self.ycor)**2) <= ball.radius+self.radius

	def collide(self, ball):
		temp = ball.xspeed
		ball.xspeed = self.xspeed
		self.xspeed = temp

		temp = ball.yspeed
		ball.yspeed = self.yspeed
		self.yspeed = temp


def position(x,y):
	x = random.randint(radius, width-radius)
	y = random.randint(radius, height-radius)
	for ball in balls:
		if math.sqrt((ball.xcor - x)**2 + (ball.ycor - y)**2) <= radius*2:
			x = random.randint(radius, width-radius)
			y = random.randint(radius, height-radius)

	return (x,y)


def convert_y(y):
	y -= height
	y *= -1
	return y


for index in range(amount):
	x = y = 0
	cor = position(x,y)
	speedx = random.random()*5
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
			if ball.collidesWith(Ball):
				ball.collide(Ball)

		ball.update()
		ball.draw(win)

	pygame.display.update()
	time.sleep(0.01)
