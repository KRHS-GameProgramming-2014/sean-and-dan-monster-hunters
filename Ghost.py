import pygame
from Creature import Creature

class Ghost(Creature):
	def __init__(self, pos):
		Creature.__init__(self, image, speed = [0,0], pos = [0,0])
		self.upImages = [pygame.image.load("RSC/Ghost/GhostUp1.png"),
							pygame.image.load("RSC/Ghost/GhostUp2.png")]
		self.downImages = [pygame.image.load("RSC/Ghost/GhostDown1.png"),
							pygame.image.load("RSC/Ghost/GhostDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Ghost/GhostLeft1.png"),
							pygame.image.load("RSC/Ghost/GhostLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Ghost/GhostRight1.png"),
							pygame.image.load("RSC/Ghost/GhostRight2.png")]
		self.facing = "down"
		self.changed = False
		self.images = self.downImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
		
	def update(self, width, height):
		Creature.update(self, width, height)
		self.animate()
		self.changed = False
		
	def collidePlayer(self, other): #do damage, don't bounce
		pass
		
	def collideDemon(self, other):
		pass
				
	def collideLeviathan(self, other):
		pass
				
	def collideBlock(self, other):
		pass
