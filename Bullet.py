import pygame, math

class Bullet():
	def __init__(self, pos, direction, damage):
		self.image = pygame.image.load("RSC/weapons/bullet.png")
		self.rect = self.image.get_rect()
		speed = 2
		if facing == "up":
			self.speedx = 0
			self.speedy = -speed
		elif facing == "down":
			self.speedx = 0
			self.speedy = speed
		elif facing == "right":
			self.speedx = speed
			self.speedy = 0
		elif facing == "up":
			self.speedx = -speed
			self.speedy = 0
		self.speed = [self.speedx, self.speedy]
		self.place(pos)
		self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
		self.living = True
		self.damage = 1
		
	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
		
	def move(self):
		self.rect = self.rect.move(self.speed)
		
	def collideWall(self, width, height):
		if self.rect.left < 0 or self.rect.right > width:
				self.living = False
		if self.rect.top < 0 or self.rect.bottom > height:
				self.living = False
		
	#def collideBall(self, other):
		#if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
			#if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
				#if (self.radius + other.radius) > self.distance(other.rect.center):
					#self.living = False
					
					#don't need?
