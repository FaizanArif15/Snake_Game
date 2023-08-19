import pygame
import os
from time import *
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill((100,125,150))

clock = pygame.time.Clock()

class SpriteSheet:
    
    def __init__(self,filename) -> None:
        self.filename = filename
        self.sprite_sheet = pygame.image.load(self.filename)
        
    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(x,y,w,h))
        
        return sprite
    
if __name__ == "__main__":
    sprite_image = SpriteSheet(os.path.join("snake game/snake_with_sprite","snake_sprite_sheet.png"))
    image1 = sprite_image.get_sprite(0,0,42,42)
    image2 = sprite_image.get_sprite(0,-42,42,40)
    image3 = sprite_image.get_sprite(0,-85,42,37)
    body = sprite_image.get_sprite(-93,-85,24,41)
    tail = sprite_image.get_sprite(-51,-85,24,41)
    
    i = 0
    run = True
    tail = pygame.transform.rotate(tail,180)
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                run =  False
            
        screen.blit(image1,(200,200))
        screen.blit(body,(160,209))
        screen.blit(tail,(118,209))
        pygame.display.update()
        screen.fill((100,125,150))
        
        screen.blit(image2,(200,200))
        screen.blit(body,(160,209))
        screen.blit(tail,(118,209))
        pygame.display.update()
        screen.fill((100,125,150))
        
        screen.blit(image3,(200,200))
        screen.blit(body,(160,209))
        screen.blit(tail,(118,209))
        pygame.display.update()
        screen.fill((100,125,150))
        i += 1
