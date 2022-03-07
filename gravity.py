import pygame
import time
import random
import math

from settings import *

balls = []

class object:
	def __init__(self, radius):
		self.color = COLORS[0]
		self.xcor = 0
		self.ycor = 0
		self.radius = radius
		self.xspeed = 0
		self.yspeed = 0

	def move(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor
	
	def update(self):
		self.yspeed -= ACCELERATION_DUE_TO_GRAVITY
		self.yspeed -= self.yspeed * AIR_DRAG_FACTOR
		self.xspeed -= self.xspeed * AIR_DRAG_FACTOR

		if self.ycor - self.radius <= 0:
			self.yspeed = abs(self.yspeed)
			
			if self.yspeed < 1:
				self.yspeed = 0
				self.xspeed -= self.xspeed * FRICTION_COEFFICIENT
				
		if self.xcor + RADIUS >= WIDTH:
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
		return ball is not self and math.sqrt((ball.xcor - self.xcor)**2 + (ball.ycor - self.ycor)**2) <= ball.radius+self.radius-ALLOWED_OVERLAP_OFFSET

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
		self.color = random.choice(COLORS)
		self.setRandomPosition()
		while self.collidesWithAny():
			self.setRandomPosition()
	
	def setRandomPosition(self):
		self.xcor = random.randint(self.radius, WIDTH - self.radius)
		self.ycor = random.randint(self.radius, HEIGHT - self.radius)
			


def convert_y(y):
	y -= HEIGHT
	y *= -1
	return y


for index in range(AMOUNT):
	ball = object(RADIUS)
	ball.randomize()
	balls.append(ball)


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity")

print("Press Space to pause, Q to exit.")

paused = False
running = True
while running:
	win.fill((255,255,255))
	
	for ball in balls:
		ball.draw(win)
	pygame.display.update()

	if not paused:
		for ball in balls:	
			ball2 = ball.collidesWithAny()
			if ball2:
				ball.collide(ball2)
			ball.update()

	time.sleep(1/FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				running = False
			elif event.key == pygame.K_SPACE:
				paused = not paused

pygame.quit()