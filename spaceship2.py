import pygame, os
from bullet import Bullet
from movement import AngleMovement
#Set working directory

#Spaceship sprite
class Spaceship2(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load('data/graphics/spaceship/spaceship2.png').convert_alpha()
        self.original_image = pygame.transform.rotozoom(self.original_image,0,0.04)
        self.image = self.original_image
        self.dx = 0
        self.dy = 0
        self.centerx = 0
        self.centery = 0
        self.rect = self.image.get_rect(center = (self.centerx,self.centery))
        self.angle = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        #Cool down system for shooting bullet
        self.last = pygame.time.get_ticks()
        self.cooldown = 200

        self.bullets = pygame.sprite.Group()  

    def RotateInput(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_LEFT]:
            self.angle = (self.angle+2) %360
        elif Keys[pygame.K_RIGHT]:
            self.angle = (self.angle-2) %360
        if Keys[pygame.K_UP]:
            self.ShootBullet()
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center = (self.centerx, self.centery)) 

    def SpaceshipMoves(self):
        #Get horizontal and vertical distance to move
        self.dx, self.dy = AngleMovement(self.angle, 6)

        #Check if ship goes out of boundary
        if (self.rect.centery <= 0) and (self.angle >=0 and self.angle < 180):
            self.rect.centery = 0
        elif (self.rect.centery >= self.screen_height) and (self.angle >= 180):
            self.rect.centery = self.screen_height 
        else:
            self.centery += self.dy
        if (self.rect.centerx <= 0) and (self.angle >= 90 and self.angle < 270):
            self.rect.centerx = 0 
        elif (self.rect.centerx >= self.screen_width) and (self.angle < 90 or self.angle > 270):
            self.rect.centerx = self.screen_width
        else:
            self.centerx += self.dx
    
    def ShootBullet(self):
        now = pygame.time.get_ticks()
        #Wait more than cool down to shoot
        if now - self.last >= self.cooldown:
            self.last = now  
            self.bullets.add(Bullet(self.angle, self.centerx,self.centery, self.screen_width, self.screen_height))
        
    def update(self):
        self.SpaceshipMoves()
        self.RotateInput()
        self.bullets.update()