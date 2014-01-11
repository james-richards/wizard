import pygame
import ui.screens.main_menu

screen = pygame.display.set_mode((640, 480))

running = True

clock = pygame.time.Clock()

screen_stack = []


screen_stack.append(ui.screens.main_menu.MainMenuScreen(screen.get_size()))

# main loop
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Hand over event handling to active screen here

        screen_stack[-1].handle(event)

    
    # render active screen
    active_render = screen_stack[-1].render()
    
    screen.blit(active_render, screen.get_rect())
    pygame.display.flip()

