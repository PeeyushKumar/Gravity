import pygame
import time
import random
import math


width = 600
height = 400
radius = 50
amount = 3
balls = []
colors = [(27, 38, 44), (15, 76, 117), (50, 130, 184)]



class object:
	def __init__(self, radius):
		self.color = colors[0]
		self.xcor = 0
		self.ycor = 0
		self.radius = radius
		self.xspeed = 0
		self.yspeed = 0

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
	
	def collidesWithAny(self):
		for ball in balls:
			if self.checkForCollision(ball):
				return ball
		return False
			
	def checkForCollision(self, ball):
		return ball is not self and math.sqrt((ball.xcor - self.xcor)**2 + (ball.ycor - self.ycor)**2) <= ball.radius+self.radius

	def collide(self, ball):
		temp = ball.xspeed
		ball.xspeed = self.xspeed
		self.xspeed = temp

		temp = ball.yspeed
		ball.yspeed = self.yspeed
		self.yspeed = temp

	def randomize(self):
		self.xspeed = (random.random()-0.5) * 5
		self.yspeed = (random.random()-0.5) * 5
		self.color = random.choice(colors)
		self.setRandomPosition()
		while self.collidesWithAny():
			self.setRandomPosition()
	
	def setRandomPosition(self):
		self.xcor = random.randint(self.radius, width-self.radius)
		self.ycor = random.randint(self.radius, height-self.radius)
			


def convert_y(y):
	y -= height
	y *= -1
	return y


for index in range(amount):
	ball = object(radius)
	ball.randomize()
	balls.append(ball)


pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravity")

running = True
while running:
	win.fill((255,255,255))
	for ball in balls:

		ball2 = ball.collidesWithAny()
		if ball2:
			ball.collide(ball2)

		ball.update()
		ball.draw(win)

	pygame.display.update()
	time.sleep(0.01)
