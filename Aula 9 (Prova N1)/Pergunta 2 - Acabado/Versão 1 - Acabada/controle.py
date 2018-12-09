import pygame
from retangulos import Retangulo

obj_retangulo = Retangulo(0, 0, 0, 0)

altura_tela = 400
largura_tela = 400

retangulos = []

# WHITE = (255, 255, 255)

tela = altura_tela, largura_tela


def cria_retangulos():

    x = 45
    y = 50

    for linha in range(6):
        for ret in range(10):
            retangulo = Retangulo(x, y, 30, 15)
            retangulo.troca_cor()
            retangulos.append(retangulo)
            x += 31
        y += 20
        x = 45


def main():

    global altura_tela
    global largura_tela

    pygame.display.set_caption("Retangulos - Pergunta 2")

    screen = pygame.display.set_mode((altura_tela, largura_tela))

    rodando = True

    cria_retangulos()

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
                print(event)

        for ret in retangulos:
            ret.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
