import pygame
from pygame.locals import *
import levels
import os

class Level_Interface:

    def __init__(self,scr,width,height,surface,ext_screen) -> None:
        
        # screen variables
        self.screen = scr
        self.screen_width = width
        self.screen_height = height
        self.surface = surface
        self.extra_screen = ext_screen

        # game variables
        self.fps = 60
        self.run = True
        self.level1 = None
        self.level2 = None
        self.level3 = None
        self.back = None
        self.check_level1 = False
        self.check_level2 = False
        self.check_level3 = False
        self.check_back = False
        self.mouse_position = (0,0)
        self.collide_list = []
        self.yellow_color = (240,252,2)
        self.blue_color = (0,0,255)
        self.red_color = (255,0,0)
        
        self.levels = levels.Levels(self.screen,self.screen_width,
                        self.screen_height,self.surface,self.extra_screen)

    def display_text(self,font="calibri", size=48,position=(0,0), color = (0,0,255),text = ""):
        
        calibri = pygame.font.SysFont(font, size)
        text = calibri.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)

    def draw_menu_screen(self,color1 = (0,0,255)):
        
        self.collide_list = []
        
        # for self.level1 button
        center = 100,self.screen_height-(self.screen_height//4)*3
        level1_rect = pygame.Rect(self.screen_width//2,self.screen_height-self.screen_height//4,180,80)
        level1_rect.center = (center)
        self.level1 = pygame.draw.rect(self.screen,self.red_color,level1_rect,width=3,border_radius=10)
        self.collide_list.append(level1_rect)
        if self.check_level1:
            self.display_text(position=center,color = color1,text="Level 1")
        else:
            self.display_text(position=center,color = self.blue_color,text="Level 1")
            
        # for self.level2 button
        center = self.screen_width//2,self.screen_height-(self.screen_height//4)*3
        level2_rect = pygame.Rect(self.screen_width//2,self.screen_height-(self.screen_height//4)*2,180,80)
        level2_rect.center = (center)
        self.level2 = pygame.draw.rect(self.screen,self.red_color,level2_rect,width=3,border_radius=10)
        self.collide_list.append(level2_rect)
        if self.check_level2:
            self.display_text(position=center,color = color1,text="Level 2")
        else:
            self.display_text(position=center,color = self.blue_color,text="Level 2")
            
        # for level3 button
        center = self.screen_width-100,self.screen_height-(self.screen_height//4)*3
        level3_rect = pygame.Rect(self.screen_width//2,self.screen_height-(self.screen_height//4)*3,180,80)
        level3_rect.center = (center)
        self.level3 = pygame.draw.rect(self.screen,self.red_color,level3_rect,width=3,border_radius=10)
        self.collide_list.append(level3_rect)
        if self.check_level3:
            self.display_text(position=center,color = color1,text="Level 3")
        else:
            self.display_text(position=center,color = self.blue_color,text="Level 3")
            
        # for self.back button
        center = 100,self.screen_height-100
        back_rect = pygame.Rect(self.screen_width//2,self.screen_height-(self.screen_height//4)*3,180,80)
        back_rect.center = (center)
        self.back = pygame.draw.rect(self.screen,self.red_color,back_rect,width=3,border_radius=10)
        self.collide_list.append(back_rect)
        if self.check_back:
            self.display_text(position=center,color = color1,text="Back")
        else:
            self.display_text(position=center,color = self.blue_color,text="Back")
            
    def initialize(self):
        
        self.levels = levels.Levels(self.screen,self.screen_width,
                        self.screen_height,self.surface,self.extra_screen)

    def check_events(self):
        
        for event in pygame.event.get():
                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.run = False
                    
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if self.level1.collidepoint(mouse_position):
                        check = self.levels.levels(1)
                        if check == False:
                            self.run = False
                        elif check != True:
                            self.initialize()
        
                            # set sound in background
                            pygame.mixer.music.load(os.path.join("start.mp3"))
                            pygame.mixer.music.play(-1)
        
                    elif self.level2.collidepoint(mouse_position):
                        check = self.levels.levels(2)
                        if check == False:
                            self.run = False
                        elif check != True:
                            self.initialize()
        
                            # set sound in background
                            pygame.mixer.music.load(os.path.join("start.mp3"))
                            pygame.mixer.music.play(-1)
                        
                        
                    elif self.level3.collidepoint(mouse_position):
                        check = self.levels.levels(3)
                        if check == False:
                            self.run = False
                        elif check != True:
                            self.initialize()
        
                            # set sound in background
                            pygame.mixer.music.load(os.path.join("start.mp3"))
                            pygame.mixer.music.play(-1)
                            
                    elif self.back.collidepoint(mouse_position):
                        return False
                
    def collide_objects(self):
        
        mouse_position = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_position[0],mouse_position[1],1,1)
        if mouse_rect.collidelist(self.collide_list) == 0:
            self.check_level1 = True 
        elif mouse_rect.collidelist(self.collide_list) == 1:
            self.check_level2 = True 
        elif mouse_rect.collidelist(self.collide_list) == 2:
            self.check_level3 = True
        elif mouse_rect.collidelist(self.collide_list) == 3:
            self.check_back = True 
                        
    def set_background(self):
        self.screen.fill((0, 0, 0))           

    def level_menu(self):
        
        while self.run:
            
            self.set_background()
            
            check = self.check_events()
            if check == True:
                return True
            elif check ==False:
                return -1
            
            if self.run == False:
                return False 
            
            if self.check_level3 or self.check_level2 or self.check_level1 or self.check_back:
                self.draw_menu_screen(self.yellow_color)
                self.check_level1 = False
                self.check_level2 = False
                self.check_level3 = False
                self.check_back = False
            else:
                self.draw_menu_screen()  
                
            self.collide_objects()
                    
            
            pygame.display.update()
        

        