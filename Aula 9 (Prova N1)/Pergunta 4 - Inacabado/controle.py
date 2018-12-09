import pygame
from bola import Bola
from retangulo import Retangulo

bola = Bola()
retangulo = Retangulo(0, 0, 0, 0)

largura_tela = 400
altura_tela = 400

screen_wh = largura_tela, altura_tela

velocidade_x = 5
velocidade_y = 5

BLACK = (0, 0, 0)

relogio = pygame.time.Clock()

retangulos = []


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
    if bola.get_centro_x() + bola.get_raio() >= largura_tela or bola.get_centro_x() - bola.get_raio() <= 0:
        velocidade_x *= -1
        bola.troca_cor()
    if bola.get_centro_y() + bola.get_raio() >= altura_tela or bola.get_centro_y() - bola.get_raio() <= 0:
        velocidade_y *= -1
        bola.troca_cor()


def cria_retangulos():
        x = 45
        y = 125
        for linha in range(6):
            for ret in range(10):
                retangulo = Retangulo(x, y, 30, 15)
                retangulo.troca_cor()
                retangulos.append(retangulo)
                x += 31
            y += 20
            x = 45


# def colisao():
#     if (bola.get_centro_x() < retangulo.self.posicao_x + bola.get_raio()) and (bola.get_centro_x() + retangulo.self.largura > retangulo.self.posicao_x) and (bola.get_centro_y() < retangulo.self.posicao_y + bola.get_raio()) and (retangulo.self.altura + bola.get_centro_y() > retangulo.self.posicao_y):
# 


def main():
    pygame.init()
    pygame.display.set_caption("Bate e morre - Pergunta 4")
    screen = pygame.display.set_mode((largura_tela, altura_tela))

    rodando = True

    cria_bola()
    cria_retangulos()

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    rodando = False
            print(event)

        pygame.draw.rect(screen, BLACK, [0, 0, altura_tela, largura_tela], )

        verifica_limites()
        bola.move(velocidade_x, velocidade_y)

        for ret in retangulos:
            ret.draw(screen)

        bola.draw(screen)
        pygame.display.flip()
        relogio.tick(30)


if __name__ == "__main__":
    main()
