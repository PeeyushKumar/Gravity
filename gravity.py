import turtle
import random


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("gravity")
wn.tracer(0)


balls = []
color=["red","yellow","orange","pink","purple","white","violet"]
shape=["circle","triangle","square"]

for bal in range(50):
	balls.append(turtle.Turtle())

for ball in balls:
	ball.shape(random.choice(shape))
	x=random.randint(-290,290)
	y=random.randint(-200,400)
	ball.goto(x,y)
	ball.color(random.choice(color))
	ball.penup()
	ball.speed(0)
	ball.dy=-1
	ball.dx=random.randint(-3,3)
	ball.dz=random.randint(-5,-5)

gravity=0.1
loop=True




while loop:
	wn.update()
	for ball in balls:
		ball.sety(ball.ycor() + ball.dy)
		ball.dy-=gravity
		ball.setx(ball.xcor() + ball.dx)
		ball.rt(ball.dz)

		if ball.xcor() > 330:
			ball.dx*=-1

		if ball.xcor() < -330:
			ball.dx*=-1

		if ball.ycor() < -270 :
			ball.sety(-270)
			ball.dy*=-1
			ball.dy-=1










wn.mainloop()
