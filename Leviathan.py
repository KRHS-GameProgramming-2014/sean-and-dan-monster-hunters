import pygame, math
from Demon import Demon


class Leviathan(Demon):
	def __init__(self, pos):
		Creature.__init__(self, "RSC/Leviathan/LeviDown1.png", [0,0], pos)
		self.upImages = [pygame.image.load("RSC/Leviathan/LeviUp1.png"),
							pygame.image.load("RSC/Leviathan/LeviUp2.png")]
		self.downImages = [pygame.image.load("RSC/Leviathan/LeviDown1.png"),
							pygame.image.load("RSC/Leviathan/LeviDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Leviathan/LeviLeft1.png"),
							pygame.image.load("RSC/Leviathan/LeviLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Leviathan/LeviRight1.png"),
							pygame.image.load("RSC/Leviathan/LeviRight2.png")]
							
	def detectPlayer(self, player):
		if self.direction == "up"
			if self.rect.right+self.detectRadius > player.rect.left:
				if self.rect.left-self.detectRadius < player.rect.right:
					if self.rect.bottom > player.rect.top:
						if self.rect.top+self.detectRadius*2 < player.rect.bottom:
							seen = True
		if self.direction == "down"
			if self.rect.right+self.detectRadius > player.rect.left:
				if self.rect.left-self.detectRadius < player.rect.right:
					if self.rect.bottom+self.detectRadius*2 < player.rect.top:
						if self.rect.top > other.rect.bottom:
							seen = True
		if self.direction == "right"
			if self.rect.right+self.detectRadius*2 > player.rect.left:
				if self.rect.left < player.rect.right:
					if self.rect.bottom+self.detectRadius < player.rect.top:
						if self.rect.top+self.detectRadius > other.rect.bottom:
							seen = True
		if self.direction == "left"
			if self.rect.right > player.rect.left:
				if self.rect.left-self.detectRadius*2 < player.rect.right:
					if self.rect.bottom+self.detectRadius < player.rect.top:
						if self.rect.top+self.detectRadius > other.rect.bottom:
							seen = True
							
		if seen:
