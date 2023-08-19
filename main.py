import pygame
from pygame.locals import *
from random import *
from pygame.math import *
import os
from time import *
from spritesheet import *
import main_menu
import asyncio

class Food:
    
    def __init__(self,surface_width,surface_height,surface) -> None:
        
        self.surface = surface
        self.surface_width = surface_width
        self.surface_height = surface_height
        
        self.food_list = [pygame.image.load(os.path.join("rat1.png")),
                        pygame.image.load(os.path.join("rat2.png")),
                        pygame.image.load(os.path.join("rat3.png")),
                        pygame.image.load(os.path.join("bird1.png")),
                        pygame.image.load(os.path.join("bird2.png")),
                        pygame.image.load(os.path.join("bird3.png")),
                        pygame.image.load(os.path.join("frog1.png")),
                        pygame.image.load(os.path.join("frog2.png")),
                        pygame.image.load(os.path.join("frog3.png")),
                        pygame.image.load(os.path.join("frog4.png")),
                        pygame.image.load(os.path.join("frog5.png")),
                        pygame.image.load(os.path.join("rabbit1.png")),
                        pygame.image.load(os.path.join("rabbit2.png")),
                        pygame.image.load(os.path.join("hamster1.png")),
                        pygame.image.load(os.path.join("gerbil1.png")),
                        pygame.image.load(os.path.join("insect1.png")),
                        pygame.image.load(os.path.join("insect2.png")),
                        pygame.image.load(os.path.join("insect3.png")),
                        pygame.image.load(os.path.join("insect4.png")),
                        pygame.image.load(os.path.join("insect5.png")),
                        ]
        
        self.food_size = 30
        self.x = randint(20,self.surface_width-20)
        self.y = randint(20,self.surface_height-20)
        self.width = self.food_size
        self.height = self.food_size
        self.food_rect = None
        self.food = self.food_list[randint(0,len(self.food_list)-1)]
        
    def rect_food(self):
        
        self.food = pygame.transform.scale(self.food,(self.width,self.height))
        self.food_rect = self.food.get_rect(center = (self.x,self.y))

    def draw_food(self):
        self.surface.blit(self.food,self.food_rect)

class Snake:
    
    def __init__(self,width,height,surface,cell_size,screen) -> None:
        
        self.surface = surface
        self.surface_width = width
        self.surface_height = height
        self.cell_size = cell_size
        
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        self.body = [Vector2(5,8),Vector2(6,8),Vector2(7,8)]
        self.width = cell_size
        self.height = cell_size
        self.direction = Vector2(1,0)
        self.snake_rect = []
        self.sprite_image = SpriteSheet(os.path.join("snake_sprite_sheet.png"))
        
    def draw_snake(self):
        
        self.snake_rect = []
        for index,body in enumerate(self.body):
            self.x = body.x * self.width
            self.y = body.y * self.height
            self.snake_rect.append(pygame.Rect(self.x,self.y,self.width,self.height))
            
            # call for head
            if index == len(self.body)-1:
                self.head()
            
            # call for tail
            elif index == 0:
                self.tail()
                
            # from left to down
            elif body.x == self.body[index+1].x and (body.x == self.body[index-1].x+1
                or (body.x == 0 and self.body[index-1].x == (self.surface_width//self.width)-1)) and \
                body.y == self.body[index-1].y and (body.y == self.body[index+1].y-1  \
                or (body.y == (self.surface_height//self.height)-1 and self.body[index+1].y == 0)):
                image = self.sprite_image.get_sprite(-84,-9,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x-8,self.y+2))
                
            # from down to left
            elif body.y == self.body[index+1].y and (body.y == self.body[index-1].y-1 \
                or (body.y == (self.surface_height//self.height)-1 and self.body[index-1].y == 0)) and \
                body.x == self.body[index-1].x and (body.x == self.body[index+1].x+1 \
                or (body.x == 0 and self.body[index+1].x == (self.surface_width//self.width)-1)):
                image = self.sprite_image.get_sprite(-84,-9,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x-7,self.y+1))
               
            # from down to right 
            elif body.y == self.body[index+1].y and (body.y == self.body[index-1].y-1 \
                or (body.y == (self.surface_height//self.height)-1) and self.body[index-1].y == 0) and \
                body.x == self.body[index-1].x and (body.x == self.body[index+1].x-1 \
                or (body.x == (self.surface_width//self.width)-1 and self.body[index+1].x == 0 )):
                image = self.sprite_image.get_sprite(-51,-9,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x+2,self.y+2)) 
                
            # from right to down
            elif body.x == self.body[index+1].x and (body.x == self.body[index-1].x-1 \
                or (body.x == (self.surface_width//self.width)-1 and self.body[index-1].x == 0)) and \
                body.y == self.body[index-1].y and (body.y == self.body[index+1].y-1 \
                or (body.y == (self.surface_height//self.height)-1 and self.body[index+1].y == 0)):
                image = self.sprite_image.get_sprite(-51,-9,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x+1,self.y+1))    
            
            # from left to up
            elif body.x == self.body[index+1].x and (body.x == self.body[index-1].x+1 \
                or (body.x == 0 and self.body[index-1].x == (self.surface_width//self.width)-1)) and \
                body.y == self.body[index-1].y and (body.y == self.body[index+1].y+1 \
                or (body.y == 0 and self.body[index+1].y == (self.surface_height//self.height)-1)):
                image = self.sprite_image.get_sprite(-84,-42,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x-7,self.y-7))
            
            # from up to left 
            elif body.y == self.body[index+1].y and (body.y == self.body[index-1].y+1 \
                or (body.y == 0 and self.body[index-1].y == (self.surface_height//self.height)-1)) and \
                body.x == self.body[index-1].x and (body.x == self.body[index+1].x+1 \
                or (body.x == 0 and self.body[index+1].x == (self.surface_width//self.width)-1 )):
                image = self.sprite_image.get_sprite(-84,-42,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x-8,self.y-8)) 
                
            # from right to up
            elif body.x == self.body[index+1].x and (body.x == self.body[index-1].x-1 \
                or (body.x == (self.surface_width//self.width)-1 and self.body[index-1].x == 0)) and \
                body.y == self.body[index-1].y and (body.y == self.body[index+1].y+1 \
                or (body.y == 0 and self.body[index+1].y == (self.surface_height//self.height)-1)):
                image = self.sprite_image.get_sprite(-51,-42,33,32)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x+2,self.y-8))
                
            # from up to right
            elif body.y == self.body[index+1].y and (body.y == self.body[index-1].y+1 \
                or (body.y == 0 and self.body[index-1].y == (self.surface_height//self.height)-1)) and \
                body.x == self.body[index-1].x and (body.x == self.body[index+1].x-1 \
                or (body.x == (self.surface_width//self.width)-1 and self.body[index+1].x == 0 )):
                image = self.sprite_image.get_sprite(-51,-42,33,33)
                image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
                self.surface.blit(image,(self.x+1,self.y-7))
            
            else:
                image = self.sprite_image.get_sprite(-93,-85,24,41)
                image = pygame.transform.scale(image,size=(self.cell_size,self.cell_size))
                
                if body.x < self.body[index+1].x:
                   image = pygame.transform.rotate(image,-90) # looking at right
                elif body.x > self.body[index+1].x:
                    image = pygame.transform.rotate(image,90) # looking at left
            
                elif body.y < self.body[index+1].y:
                    image = pygame.transform.rotate(image,180) # looking at up 
                elif body.y > self.body[index+1].y:
                    image = pygame.transform.rotate(image,0) # looking at down
        
                self.surface.blit(image,(self.x,self.y))
            
    def head(self):
        
            image = self.sprite_image.get_sprite(0,0,42,42)
            image = pygame.transform.scale(image,size=(self.cell_size+5,self.cell_size+5))
            if self.direction.x == 1:
                image = pygame.transform.rotate(image,90) # looking at right
                self.surface.blit(image,(self.x-5,self.y))
            elif self.direction.x == -1:
                image = pygame.transform.rotate(image,-90) # looking at left
                self.surface.blit(image,(self.x,self.y-2))
                
            elif self.direction.y == 1:
                image = pygame.transform.rotate(image,0) # looking at down 
                self.surface.blit(image,(self.x-3,self.y-5))
            elif self.direction.y == -1:
                image = pygame.transform.rotate(image,180) # looking at up
                self.surface.blit(image,(self.x-2,self.y+5))
                
    
    def tail(self):
        image = self.sprite_image.get_sprite(-51,-85,24,41)
        image = pygame.transform.scale(image,size=(self.cell_size,self.cell_size))
        if self.body[0].x < self.body[1].x:
            image = pygame.transform.rotate(image,-90) # looking at right
        elif self.body[0].x > self.body[1].x:
            image = pygame.transform.rotate(image,90) # looking at left
            
        elif self.body[0].y < self.body[1].y:
            image = pygame.transform.rotate(image,180) # looking at up 
        elif self.body[0].y > self.body[1].y:
            image = pygame.transform.rotate(image,0) # looking at down
        self.surface.blit(image,(self.x,self.y))
    
    def move_snake(self):
        self.body.pop(0)
        self.body.append(self.body[len(self.body)-1] + self.direction)
        
    def increase_snake(self):
         self.body.append(self.body[len(self.body)-1] + self.direction)
         
    def check_position(self):
        
        for i,body in enumerate(self.body):
            self.x = body.x * self.width
            self.y = body.y * self.height
            
            if self.x >= self.surface_width:
                self.body[i].x = 0
            elif self.x < 0:
                self.body[i].x = (self.surface_width//self.width) - 1
            elif self.y >= self.surface_height:
                self.body[i].y = 0
            elif self.y < 0:
                self.body[i].y = (self.surface_height//self.height) - 1


class Game:
    
    def __init__(self,width,height,cell_size=25,surface = None,screen = None,ext_screen=200):
        
        # screen variables
        if screen != None:
            self.screen = screen
        
        self.extra_screen = ext_screen
        self.screen_width = width + self.extra_screen
        self.screen_height = height 
        
        # surface variables
        self.surface = surface
        self.surface_width = width
        self.surface_height = height
        
        # object of main_menu
        self.main_menu = None
        
        # game variables
        self.cell_size = cell_size        
        self.game_end = False
        self.score = 0
        self.check_button = False
        self.button_rect = None
        self.yellow_color = (240,252,2)
        self.blue_color = (0,0,255)
        # objects
        self.snake = None
        self.food = None

        self.background_list = [pygame.image.load(os.path.join("background1.jpg")),
                            pygame.image.load(os.path.join("background2.jpg")),
                            pygame.image.load(os.path.join("background3.jpg")),
                            pygame.image.load(os.path.join("background4.jpg"))
                            ]
                        
        self.sound_list = [pygame.mixer.Sound("bite.mp3")]

        # game loop
        self.run = True


        # control frames per second
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        self.screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.screen_update,180)

    # set game over image
    def gameover_image(self):
        gameover = pygame.image.load(os.path.join("gameover.png"))
        gameover = pygame.transform.scale(gameover,(150,150))
        gameover_rect = gameover.get_rect(center = (self.surface_width//2,self.surface_height//2))
        return gameover,gameover_rect

    def check_events(self):
        
        for event in pygame.event.get():
                
                if event.type == self.screen_update:
                        self.snake.move_snake()
                
                    
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.run = False
                    return
                
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    if self.snake.direction != Vector2(-1,0):
                        self.snake.direction = Vector2(1,0)
                        # self.snake.move_snake()
                        
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    if self.snake.direction != Vector2(1,0):
                        self.snake.direction = Vector2(-1,0)
                        # self.snake.move_snake()
                        
                elif event.type == KEYDOWN and event.key == K_UP:
                    if self.snake.direction != Vector2(0,1):
                        self.snake.direction = Vector2(0,-1)
                        # self.snake.move_snake()
                        
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    if self.snake.direction != Vector2(0,-1):
                        self.snake.direction = Vector2(0,1)
                        # self.snake.move_snake()
                        
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if self.button_rect.collidepoint(mouse_position):
                        return True
                
    # make objects of snake and food class
    def initialize(self):
        
        self.snake = Snake(self.surface_width,self.surface_height,
                           self.surface,self.cell_size,self.screen)
        self.food = Food(self.surface_width,self.surface_height,self.surface)
        self.main_menu = main_menu.Menu(self.screen,self.screen_width,
                                        self.screen_height,self.surface,self.extra_screen)
        
        self.check_food_collide()
        
    def set_background_for_screen(self):
        
        self.screen.fill((0,0,0))
    
    def set_background_for_surface(self,index):
        
        image = self.background_list[index]
        image_rect = image.get_rect(topleft=(0,0))
        self.surface.blit(image,image_rect)
    
    def game_exit(self):
        
        # gameover image
        gameover,gameover_rect = self.gameover_image()
        self.surface.blit(gameover,gameover_rect)
        self.screen.blit(self.surface,(self.extra_screen,0))
        pygame.display.update()
        
        self.game_end = False
        self.initialize()
        self.score = 0
        second_loop = True
        while second_loop:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.run = False
                    return
                elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    second_loop = False
                    
    def display_score(self):
        
        self.main_menu.display_text(size=25,position=(100,100),color=(143,52,235),text_for_button="Your Score")
        self.main_menu.display_text(size=25,position=(100,150),color=(235,134,52),text_for_button=f"{self.score}")
        
    def draw_button(self,text = "Menu"):
        
        # for exit button
        center = 100,self.surface_height-100
        self.button_rect = pygame.Rect(100,250,107,48)
        self.button_rect.center = (center)
        
        if self.check_button:
            self.main_menu.display_text(size=20,position=center,color = self.yellow_color,text_for_button=text)
            self.check_button = False
        else:
            self.main_menu.display_text(size=20,position=center,color = self.blue_color,text_for_button=text)
        
    def check_collide_for_button(self):
        
        mouse_position = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_position[0],mouse_position[1],1,1)
        if mouse_rect.colliderect(self.button_rect):
            self.check_button = True
            
    def check_food_collide(self):
        while True:
            self.food.x = randint(20,self.surface_width-20)
            self.food.y = randint(20,self.surface_height-20)
            self.food.rect_food()
            if not self.food.food_rect.collidelistall(self.snake.snake_rect):
                break
            
    def play_sound(self):
        
        # set sound in background
        pygame.mixer.music.load(os.path.join("background.mp3"))
        pygame.mixer.music.play(-1)

    async def main(self):
        
        # initialize snake and food class
        self.initialize()
        
        self.run = self.main_menu.main_menu()
    
        self.play_sound()
        
        self.check_food_collide()
        
        # game loop
        while self.run:
            
            self.set_background_for_screen()
            self.set_background_for_surface(1)
            
            # control FPS
            self.clock.tick_busy_loop(self.fps)
                    
            self.snake.check_position()
            
            self.snake.draw_snake()        
                
            self.food.draw_food()
            
            self.display_score()
            
            self.draw_button()
            
            self.check_collide_for_button()
            
            # find event
            check = self.check_events()
            
            if check==True:
                self.run = self.main_menu.main_menu()
                if self.run:
                    self.score = 0
                    self.initialize()
                    self.play_sound()
                continue
        
            if self.run==False:
                continue    
            
            if self.snake.snake_rect[-1].colliderect(self.food.food_rect):
                self.sound_list[0].play()
                self.snake.increase_snake()
                self.score += 1
                self.food.food = self.food.food_list[randint(0,len(self.food.food_list)-1)]
                self.check_food_collide()
                
            if self.snake.snake_rect[-1].collidelistall(self.snake.snake_rect[:-1]):
                self.game_end = True
                
            if self.game_end:
                self.game_exit()
            
            self.screen.blit(self.surface,(self.extra_screen,0))
            pygame.display.update()
            await asyncio.sleep(0)
            
        
if __name__ == "__main__":
    
    # initialize pygame and mixer
    pygame.init()
    pygame.mixer.init()
    
    # surface variables
    surface_width = 600
    surface_height = 500

    # set screen
    extra_screen = 200
    screen = pygame.display.set_mode((surface_width+extra_screen,surface_height))

    # set surface
    surface = pygame.Surface((surface_width,surface_height))

    # set display
    pygame.display.set_caption("Snake Game")
    
    cell_size = 25
    
    game = Game(width=surface_width,height=surface_height,cell_size=cell_size
                ,surface=surface,screen=screen,ext_screen=extra_screen)
    asyncio.run(game.main())
    