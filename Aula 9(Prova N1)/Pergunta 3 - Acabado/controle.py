import pygame
from rebatedor import Rebatedor
pygame.init()

obj_rebatedor = Rebatedor(180, 380, 30, 15)

altura_tela = 400
largura_tela = 400


def main():
    global altura_tela
    global largura_tela

    pygame.display.set_caption("Rebatedor - Pergunta 3")

    screen = pygame.display.set_mode((altura_tela, largura_tela))

    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Apertei o ESC")
                    rodando = False
                elif pygame.key.get_pressed()[pygame.K_UP]:
                    obj_rebatedor.move_cima(altura_tela)
                    print("Apertei para cima")
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    obj_rebatedor.move_baixo()
                    print("Apertei para baixo")
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    obj_rebatedor.move_direta(largura_tela)
                    print("Apertei para direita")
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    obj_rebatedor.move_esquerda()
                    print("Apertei para esquerda")
            print(event)

        pygame.draw.rect(screen, (0, 0, 0), [0, 0, altura_tela, largura_tela], )
        obj_rebatedor.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
