import pygame

screen = pygame.display.set_mode((640, 480))

running = True

clock = pygame.time.Clock()


# main loop
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




