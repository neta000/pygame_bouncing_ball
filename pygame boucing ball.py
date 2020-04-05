import pygame
import time
pygame.init()

class plate(object):
	def __init__(self,x,y,w,h):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.v = 5
		self.hitbox =(self.x,self.y,self.w,self.h)
	def draw(self,win):
		pygame.draw.rect(win,(55,66,55),(self.x,self.y,self.w,self.h))
		self.hit =(self.x,self.y,self.w,self.h)

class ball_class(object):
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r
		self.x_change = 1
		self.y_change = 1
		self.v = 5
		self.hitbox = (self.x,self.y,self.r)
	def move(self):
		self.x = self.x + self.v*self.x_change
		self.y = self.y + self.v*self.y_change
		if self.x > win_size[0] - self.r or self.x < self.r:
			self.x_change *= -1
		if self.y > win_size[1] - self.r or self.y < self.r:
			self.y_change *= -1
	def draw(self,win):
		pygame.draw.circle(win,(255,255,255),(self.x,self.y),self.r)
		self.move()
		self.hit = (self.x,self.y,self.r)
	def collision(self):
		self.y_change *= -1

win_size = (500,500)

win = pygame.display.set_mode(win_size);
pygame.display.set_caption("ball");

rect = plate(400,win_size[1]-30,win_size[0]/8,10)
ball = ball_class(100,10,5)
run = True
while run:
	pygame.time.delay(20)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	if ball.x - ball.r < rect.x + rect.w and ball.x + ball.r > rect.x:
		if ball.y + ball.r == rect.y:
			ball.collision()
	keys =pygame.key.get_pressed()
	if keys[pygame.K_RIGHT] and rect.x + rect.v + rect.w < win_size[0]:
		rect.x += rect.v
	if keys[pygame.K_LEFT] and rect.x - rect.v > 0:
		rect.x -= rect.v
	win.fill((0,0,0));
	rect.draw(win)
	ball.draw(win)
	pygame.display.update();

pygame.quit()