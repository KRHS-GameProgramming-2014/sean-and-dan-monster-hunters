import pygame, math
from Leviathan import Leviathan
from Ghost import Ghost

class Pestilence(Demon):
    def __init__(self, pos):
        Demon.__init__(self, pos)
        self.upImages = [pygame.image.load("RSC/Boss/PestilenceUp1.png"),
                         pygame.image.load("RSC/Boss/PestilenceUp2.png")]
        self.downImages = [pygame.image.load("RSC/Boss/PestilenceDown1.png"),
                           pygame.image.load("RSC/Boss/PestilenceDown2.png")]
        self.leftImages = [pygame.image.load("RSC/Boss/PestilenceLeft1.png"),
                           pygame.image.load("RSC/Boss/PestilenceLeft2.png")]
        self.rightImages = [pygame.image.load("RSC/Boss/PestilenceRight1.png"),
                            pygame.image.load("RSC/Boss/PestilenceRight2.png")]
        
        self.detectionRadius = 150
        
        if math.fabs(self.speedx) >= math.fabs(self.speedy):
                if self.speedx >= 0:
                    self.facing = "right"
                else:
                    self.facing = "left"
        else:
            if self.speedy >= 0:
                self.facing = "down"
            else:
                self.facing = "up"
                
    def move(self, players):
        for player in players:
            self.detect(player)
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def update(self, width, height, players):
        if self.didBounceX or self.didBounceY:
            self.changed = True
        if math.fabs(self.speedx) >= math.fabs(self.speedy):
            if self.speedx >= 0:
                self.facing = "right"
            else:
                self.facing = "left"
        else:
            if self.speedy >= 0:
                self.facing = "down"
            else:
                self.facing = "up"            
        self.move(players)
        self.collideWall(width, height)
        self.animate()
        self.changed = False
        self.didBounceX = False
        self.didBounceY = False
    
    def collidePlayer(self, other):
        hurt(player)
        
    #The following code was written by Dominic Flanders
    
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                
    def detect(self, player):
        if self.distToPoint(player.rect.center) < self.detectionRadius:
            pX = player.rect.center[0]
            pY = player.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
           
            if pX > zX:
                self.speedx = self.maxSpeed
            elif pX < zX:
                self.speedx = -self.maxSpeed
            else:
                self.speedx = 0
       
            if pY > zY:
                self.speedy = self.maxSpeed
            elif pY < zY:
                self.speedy = -self.maxSpeed
            else:
                self.speedy = 0
    

        


