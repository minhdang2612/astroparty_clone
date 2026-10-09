import pygame, os
from movement import AngleMovement
#Set working directory

class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, x, y, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load('data/graphics/bullet/bullet1.png').convert_alpha()
        self.original_image = pygame.transform.rotozoom(self.original_image,0,0.3)
        self.image = self.original_image
        self.centerx = x
        self.centery = y
        self.rect = self.image.get_rect(center = (self.centerx, self.centery))
        self.screen_width = screen_width
        self.screen_height = screen_height

        #Calculate directions to move in
        self.angle = angle
        self.dx, self.dy = AngleMovement(self.angle, 9)

    def BulletRotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center = (self.centerx, self.centery)) 

    def BulletMove(self):
        self.centerx += self.dx
        self.centery += self.dy

    def Destroy(self):
        if (self.rect.y <= -50) or (self.rect.y > self.screen_height+10)  or (self.rect.x <= -50) or (self.rect.x > self.screen_width+10):
            self.kill()

    def update(self):
        self.BulletRotate()
        self.BulletMove()
        self.Destroy()