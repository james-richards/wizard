import pygame

screen = pygame.display.set_mode((640, 480))

running = True


while running:
    event = pygame.event.poll()
    screen.fill((255, 0, 0))
    if event.type == pygame.QUIT:
        running = False




