import pygame   
from sys import exit
from spaceship import Spaceship
from spaceship2 import Spaceship2

class Game:
    def __init__(self):
        spaceship = Spaceship(screen_width, screen_height)
        self.spaceship = pygame.sprite.GroupSingle(spaceship)
        spaceship2 = Spaceship2(screen_width, screen_height)
        self.spaceship2 = pygame.sprite.GroupSingle(spaceship2)
    def run(self):
        self.spaceship.draw(screen)
        self.spaceship.sprite.bullets.draw(screen)
        self.spaceship2.draw(screen)
        self.spaceship2.sprite.bullets.draw(screen)

        self.spaceship.update()
        self.spaceship2.update()

#Main game loop
if __name__ == '__main__':
    pygame.init
    clock = pygame.time.Clock()
    game_active = True

    #Display
    pygame.display.set_caption("Astro Party")
    screen_width = 930
    screen_height = 930
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_active:
            screen.fill('Grey')
            game.run()

        pygame.display.update()
        clock.tick(60)