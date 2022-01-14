import turtle #graphics module
import pygame #needed to play mp3 files
pygame.mixer.init()

window = turtle.Screen()
window.title("Pong by RevelKnievel")
window.bgcolor("green")
window.setup(width = 800, height = 600)
window.tracer(0) #stops window from updating; must be manually updated; speeds up game

#score
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets speed of animation
paddle_a.shape("square")
paddle_a.shapesize(5, 1)
paddle_a.color("black")
paddle_a.penup() #no drawing when moving
paddle_a.goto(-350, 0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(5, 1)
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball_dx = 0.3 #ball movement increments in pixels
ball_dy = 0.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align = "center", font = ("Courier", 20, "normal"))

def paddle_a_up():
	y = paddle_a.ycor() #returns y coordinate
	y += 20
	paddle_a.sety(y) #sets paddle a's y coordinate to the new y

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)
	
def paddle_b_down():
	paddle_b.sety(paddle_b.ycor() - 20)

#keybinding
window.listen() #tells screen to listen for keyboard input
window.onkeypress(paddle_a_up, "w") #binds function to key. Case specific
window.onkeypress(paddle_a_up, "W")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_a_down, "S")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
	window.update() #updates the screen

	#move the ball
	ball.setx(ball.xcor() - ball_dx)
	ball.sety(ball.ycor() + ball_dy)

	#ball border check
	if ball.ycor() > 288:
		ball.sety(288)
		ball_dy *= -1
		pygame.mixer.music.load("Explosion+1.mp3")
		pygame.mixer.music.play()

	if ball.ycor() < -282:
		ball.sety(-282)
		ball_dy *= -1
		pygame.mixer.music.play()
		
	if ball.xcor() > 382:
		ball.goto(0, 0)
		ball_dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align = "center", font = ("Courier", 20, "normal"))
		
	if ball.xcor() < -388:
		ball.goto(0, 0)
		ball_dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {0} Player B: {1}".format(score_a, score_b), align = "center", font = ("Courier", 20, "normal"))
	
	#paddle border check
	if paddle_a.ycor() > 248:
		paddle_a.sety(248)
		
	if paddle_a.ycor() < -242:
		paddle_a.sety(-242)
		
	if paddle_b.ycor() < -242:
		paddle_b.sety(-242)	
		
	if paddle_b.ycor() > 248:
		paddle_b.sety(248)

	#paddle and ball collision
	if (ball.xcor() > 335 and ball.xcor() < 337) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
		ball.setx(335)
		ball_dx *= -1
		pygame.mixer.music.play()
		
	if (ball.xcor() < -333 and ball.xcor() > -335) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
		ball.setx(-333)
		ball_dx *= -1
		pygame.mixer.music.play()
