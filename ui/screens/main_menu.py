import ui.screens.screen
import pygame

class MainMenuScreen(ui.screens.screen.GameScreen):
    
    def render(self):
        surface = pygame.Surface((320, 240))
        surface.fill((255,0,0))
        return surface


