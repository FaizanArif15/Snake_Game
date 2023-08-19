import pygame
from pygame.locals import *
import os
import level_interface

class Menu:
    
    def __init__(self,screen,width,height,surface,ext_screen) -> None:
        
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.surface = surface
        self.extra_screen = ext_screen

        self.lvl_interface = level_interface.Level_Interface(self.screen,
                                self.screen_width,self.screen_height
                                ,self.surface,self.extra_screen)
        
        # game variables
        self.fps = 60
        self.run = True
        self.exit = None
        self.level = None
        self.prac = None
        self.check_exit = False
        self.check_prac = False
        self.check_levels = False
        self.mouse_position = (0,0)
        self.collide_list = []
        self.yellow_color = (240,252,2)
        self.blue_color = (0,0,255)
        self.red_color = (255,0,0)

    def display_text(self, color,font="calibri", size=48,position=(0,0),
                    text_for_button = ""):
        
        calibri = pygame.font.SysFont(font, size)
        text = calibri.render(text_for_button, True, color)
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)

    def draw_menu_screen(self,color1 = (0,0,255)):
        
        self.collide_list = []
        
        # for exit button
        center = self.screen_width//2,self.screen_height-self.screen_height//4
        exit_rect = pygame.Rect(self.screen_width//2,self.screen_height-self.screen_height//4,180,80)
        exit_rect.center = (center)
        self.exit = pygame.draw.rect(self.screen,self.red_color,exit_rect,width=3,border_radius=10)
        self.collide_list.append(exit_rect)
        if self.check_exit:
            self.display_text(position=center,color = color1,text_for_button="Exit")
        else:
            self.display_text(position=center,color = self.blue_color,text_for_button="Exit")
            
        # for Practice button
        center = self.screen_width//2,self.screen_height-(self.screen_height//4)*2
        prac_rect = pygame.Rect(self.screen_width//2,self.screen_height-(self.screen_height//4)*2,180,80)
        prac_rect.center = (center)
        self.prac = pygame.draw.rect(self.screen,self.red_color,prac_rect,width=3,border_radius=10)
        self.collide_list.append(prac_rect)
        if self.check_prac:
            self.display_text(position=center,color = color1,text_for_button="Practice")
        else:
            self.display_text(position=center,color = self.blue_color,text_for_button="Practice")
            
        # for levels button
        center = self.screen_width//2,self.screen_height-(self.screen_height//4)*3
        level_rect = pygame.Rect(self.screen_width//2,self.screen_height-(self.screen_height//4)*3,180,80)
        level_rect.center = (center)
        self.level = pygame.draw.rect(self.screen,self.red_color,level_rect,width=3,border_radius=10)
        self.collide_list.append(level_rect)
        if self.check_levels:
            self.display_text(position=center,color = color1,text_for_button="Levels")
        else:
            self.display_text(position=center,color = self.blue_color,text_for_button="Levels")
        

    def check_events(self):
        
        for event in pygame.event.get():
                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.run = False
                    
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if self.exit.collidepoint(mouse_position):
                        self.run = False
                    elif self.prac.collidepoint(mouse_position):
                        return True
                    elif self.level.collidepoint(mouse_position):
                        check = self.lvl_interface.level_menu()
                        if check == False:
                            self.run = False
                        elif check != True:
                            self.initialize()
    
    def initialize(self):
        self.lvl_interface = level_interface.Level_Interface(self.screen,
                                self.screen_width,self.screen_height
                                ,self.surface,self.extra_screen)            
    
    def collide_objects(self):
        
        mouse_position = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_position[0],mouse_position[1],1,1)
        if mouse_rect.collidelist(self.collide_list) == 0:
            self.check_exit = True 
        elif mouse_rect.collidelist(self.collide_list) == 1:
            self.check_prac = True 
        elif mouse_rect.collidelist(self.collide_list) == 2:
            self.check_levels = True 
                        
    def set_background(self):
        self.screen.fill((0, 0, 0))           

    def main_menu(self):

        # set sound in background
        pygame.mixer.music.load(os.path.join("start.mp3"))
        pygame.mixer.music.play(-1)
        
        while self.run:
            
            self.set_background()
            
            if self.check_levels or self.check_prac or self.check_exit:
                self.draw_menu_screen(self.yellow_color)
                self.check_exit = False
                self.check_prac = False
                self.check_levels = False
            else:
                self.draw_menu_screen()  
                
            check = self.check_events()
            if check == True:
                return True
            if self.run == False:
                return False
            
            self.collide_objects()
                    
            
            pygame.display.update()
