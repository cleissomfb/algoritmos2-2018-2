"""Classe Retângulo"""


class Retangulo:

    def __init__(self, coorX, coorY, largura, altura):
        self.posicao_x = coorX
        self.posicao_y = coorY
        self.largura = largura
        self.altura = altura
        self.cor = 0

    def set_posicao_x(self, coordenadaX):
            self.posicao_x = coordenadaX

    def set_posicao_y(self, coordenadaY):
            self.posicao_y = coordenadaY

    def set_largura(self, largura):
        self.largura = largura

    def set_altura(self, altura):
        self.altura = altura

    def get_posicao_x(self):
        return self.posicao_x

    def get_posicao_y(self):
        return self.posicao_y

    def get_largura(self):
        return self.largura

    def get_altura(self):
        return self.altura

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, self.cor, [self.posicao_x, self.posicao_y, self.largura, self.altura])

    def troca_cor(self):
        import random
        cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        self.cor = random.choice(cores)
