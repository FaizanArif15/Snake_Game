import pygame
from pygame.locals import *
import main
import random as r

class Levels:
    
    def __init__(self,screen,width,height,surface,ext_screen) -> None:
        
        self.screen = screen
        self.surface_width = width-ext_screen
        self.surface_height = height
        self.surface = surface
        self.extra_screen = ext_screen
        
        self.collide_list = []
        self.color_level1 = (133,106,53)
        self.color_level2 = (150,100,200)
        self.color_level3 = (239,252,2)
        
        self.main_logic = main.Game(self.surface_width,self.surface_height,
                        surface=self.surface,screen=self.screen,
                        ext_screen=self.extra_screen)
        
    def border_collide(self):
        if self.main_logic.snake.snake_rect[-1].collidelistall(self.collide_list):
            return True
        
    def level_no1(self):
        
        self.collide_list= []
        
        for i in range(self.surface_width):
                # upper border
            border_rect = pygame.Rect(i*10,0,20,25)
            self.border = pygame.draw.rect(self.surface,self.color_level1,border_rect)
            self.collide_list.append(border_rect)
                
            # lower border
            border_rect = pygame.Rect(i*10,self.surface_height-25,20,25)
            self.border = pygame.draw.rect(self.surface,self.color_level1,border_rect)
            self.collide_list.append(border_rect)
                
            # left border
            border_rect = pygame.Rect(0,i*10,25,20)
            self.border = pygame.draw.rect(self.surface,self.color_level1,border_rect)
            self.collide_list.append(border_rect)
                
            # right border
            border_rect = pygame.Rect(self.surface_width-25,i*10,25,20)
            self.border = pygame.draw.rect(self.surface,self.color_level1,border_rect)
            self.collide_list.append(border_rect)
        
    def level_no2(self):
        
        self.collide_list= []
        
        for i in range(100,self.surface_width-102):
            
                # upper border
                border_rect = pygame.Rect(i,0,3,25)
                self.border = pygame.draw.rect(self.surface,self.color_level2,border_rect)
                self.collide_list.append(border_rect)
                
                # lower border
                border_rect = pygame.Rect(i,self.surface_height-25,3,25)
                self.border = pygame.draw.rect(self.surface,self.color_level2,border_rect)
                self.collide_list.append(border_rect)
                
                if i < self.surface_height-102:
                    # left border       
                    border_rect = pygame.Rect(0,i,25,3)
                    self.border = pygame.draw.rect(self.surface,self.color_level2,border_rect)
                    self.collide_list.append(border_rect)
                    
                    # right border
                    border_rect = pygame.Rect(self.surface_width-25,i,25,3)
                    self.border = pygame.draw.rect(self.surface,self.color_level2,border_rect)
                    self.collide_list.append(border_rect)
                    
    def level_no3(self):
        
        self.collide_list= []
        
        for i in range(100,400,90):
            
                # upper left hurdle 
                border_rect = pygame.Rect(i,100,103,50)
                self.border = pygame.draw.rect(self.surface,self.color_level3,border_rect)
                self.collide_list.append(border_rect)
                
                # lower left hurdle
                border_rect = pygame.Rect(i,self.surface_height-150,103,50)
                self.border = pygame.draw.rect(self.surface,self.color_level3,border_rect)
                self.collide_list.append(border_rect)
                
                # # lower right border
                border_rect = pygame.Rect(426,100,47,250)
                self.border = pygame.draw.rect(self.surface,self.color_level3,border_rect)
                self.collide_list.append(border_rect)
                    
    def levels(self,lvl):
        
        # check level no
        self.level = lvl
        
        self.main_logic.initialize()
        
        self.main_logic.play_sound()
        
        self.main_logic.check_food_collide()
        
        while self.main_logic.run:  
            
            # set backgrounds
            self.main_logic.set_background_for_screen()
            
            if self.level == 1:
                self.main_logic.set_background_for_surface(0)
                self.level_no1()
            elif self.level == 2:
                self.main_logic.set_background_for_surface(2)
                self.level_no2()
            elif self.level == 3:
                self.main_logic.set_background_for_surface(3)
                self.level_no3()
            
            self.main_logic.snake.check_position()
            
            self.main_logic.snake.draw_snake()
            
            while True:
                if not self.main_logic.food.food_rect.collidelistall(self.collide_list):
                    self.main_logic.food.draw_food()
                    break
                else:
                    self.main_logic.check_food_collide() 
            
            self.main_logic.display_score()
            
            self.main_logic.draw_button(text="Back")
            
            self.main_logic.check_collide_for_button()
            
            
            # find event
            check = self.main_logic.check_events()
            if check == True:
                return -1
            elif check ==False:
                return -1
            
            if self.main_logic.run == False:
                return False   
            
            if self.border_collide():
                self.main_logic.game_exit()
                continue
                
            
            if self.main_logic.snake.snake_rect[-1].colliderect(self.main_logic.food.food_rect):
                self.main_logic.snake.increase_snake()
                self.main_logic.score += 1
                self.main_logic.food.food = self.main_logic.food.food_list[r.randint(0,len(self.main_logic.food.food_list)-1)]
                self.main_logic.check_food_collide()
                
            if self.main_logic.snake.snake_rect[-1].collidelistall(self.main_logic.snake.snake_rect[:-1]):
                self.main_logic.game_end = True
                
            if self.main_logic.game_end:
                self.main_logic.game_exit()
            
            self.main_logic.screen.blit(self.main_logic.surface,(self.main_logic.extra_screen,0))
            pygame.display.update()
            
            
            
            
            
            