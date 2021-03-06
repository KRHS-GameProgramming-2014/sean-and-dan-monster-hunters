import pygame, math
from Bullet import Bullet


class Creature():
    def __init__(self, image, speed = [0,0], pos = [0,0], health = 1, maxHealth = 1):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.facing = "up"
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        self.health = health
        self.maxHealth = maxHealth
        self.place(pos)
        self.hurting = False
        self.hurtingFrame = 0
        self.hurtingFrameMax = 1
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
        
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            if self.hurting:
                if self.hurting:
                    if self.hurtingFrame < self.hurtingFrameMax:
                        self.hurtingFrame += 1
                    else:
                        self.hurtingFrame = 0
                        self.hurting = False
                                
        if self.changed:    
            if self.facing == "up":
                if self.hurting:
                    self.images = self.upHurtImages
                else:
                    self.images = self.upImages
            elif self.facing == "down":
                if self.hurting:
                    self.images = self.downHurtImages
                else:
                    self.images = self.downImages
            elif self.facing == "right":
                if self.hurting:
                    self.images = self.rightHurtImages
                else:
                    self.images = self.rightImages
            elif self.facing == "left":
                if self.hurting:
                    self.images = self.leftHurtImages
                else:
                    self.images = self.leftImages
            
            if self.hurting:
                self.image = self.images[self.hurtingFrame]
            else:
                self.image = self.images[self.frame]

            
    def hurt(self, amount=1):
        self.health -= amount
        self.changed = True
        self.hurting = True
        if self.health <=0:
            self.living = False
            
    def heal(self, amount=1):
        self.health += amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth
            
    def collideBullet(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.hurt(other.damage) 
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
        
