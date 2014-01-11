import ui.screens.screen
import ui.widgets.buttons
import pygame

class MainMenuScreen(ui.screens.screen.GameScreen):

    def __init__(self, size):
        
        ui.screens.screen.GameScreen.__init__(self,size)
        
        self.buttons = []
        self.buttons.append(ui.widgets.buttons.MainMenuButton("button1", pygame.Rect(0,0,100,50), self.button1action))
        self.bgcol = (255,0,0)
    
    def render(self):
        surface = pygame.Surface(self.size)
        surface.fill(self.bgcol)
        
        for button in self.buttons:
            surface.blit(button.render(), button.rect)
        
        return surface

    def handle(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mpos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.rect.collidepoint(mpos):
                    button.activate()


    def button1action(self):
        self.bgcol = (0,0,255)
