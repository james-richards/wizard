import ui.screens.screen
import pygame

class MainMenuScreen(ui.screens.screen.GameScreen):
    
    def render(self):
        surface = pygame.Surface(self.size)
        surface.fill((255,0,0))
        return surface


