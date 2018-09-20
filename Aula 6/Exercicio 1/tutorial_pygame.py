import pygame


def main():
    pygame.init()
    pygame.display.set_caption("PyGame Tutorial")

    screen = pygame.display.set_mode((800, 600))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


if __name__ == "__main__":
    main()
