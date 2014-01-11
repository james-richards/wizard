'''
Created on 11/01/2014

@author: James
'''
import pygame

class MainMenuButton():
    
    def __init__(self, text, rect, action):
        self.text = text
        self.rect = rect
        self.action = action
        
        self.surface = pygame.Surface(self.rect.size)
        

    def render(self):
        
        self.surface.fill((0,255,0))
        return self.surface
    
    def activate(self):
        self.action()



    
