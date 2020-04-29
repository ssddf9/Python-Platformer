def ready(lvl, screen):
    import pygame
    screen.fill((0, 0, 255))
    pygame.font.init()
    fontToUse = pygame.font.SysFont('Courier New Bold.ttf', 286)
    text = fontToUse.render('Ready?', False, (0, 255, 0))
    screen.blit(text, (screen.get_size()[0] / 6, screen.get_size()[1] / 6))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        mp = pygame.mouse.get_pressed()
        if mp[0]:
            return
        pygame.display.flip()