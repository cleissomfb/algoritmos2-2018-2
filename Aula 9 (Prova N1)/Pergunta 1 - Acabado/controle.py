import pygame
from bolas import Bola
pygame.init()

bola = Bola()

width = 400
height = 400

screen_wh = width, height

velocidade_x = 5
velocidade_y = 5

BLACK = (0, 0, 0)

relogio = pygame.time.Clock()


def cria_bola():

    pos_x = 200
    pos_y = 380
    raio = 20

    bola.set_centro_x(pos_x)
    bola.set_centro_y(pos_y)
    bola.set_raio(raio)

    print("setX", bola.get_centro_x())
    print("setY", bola.get_centro_y())
    print("setR", bola.get_raio())

    return bola


def verifica_limites():
    global velocidade_x
    global velocidade_y
    if bola.get_centro_x() + bola.get_raio() >= width or bola.get_centro_x() - bola.get_raio() <= 0:
        velocidade_x *= -1
        bola.troca_cor()
    if bola.get_centro_y() + bola.get_raio() >= height or bola.get_centro_y() - bola.get_raio() <= 0:
        velocidade_y *= -1
        bola.troca_cor()


def main():

    pygame.display.set_caption("Bolas - Pergunta 1")

    screen = pygame.display.set_mode((width, height))

    rodando = True

    cria_bola()
    print("setX_main", bola.get_centro_x())
    print("setY_main", bola.get_centro_y())
    print("setR_main", bola.get_raio())

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
            print(event)

        print("Valor X: ", bola.get_centro_x())
        print("Valor Y: ", bola.get_centro_y())

        verifica_limites()
        bola.move(velocidade_x, velocidade_y)

        pygame.draw.rect(screen, BLACK, [0, 0, height, width], )
        bola.draw(screen)

        pygame.display.flip()
        relogio.tick(30)


if __name__ == "__main__":
    main()
