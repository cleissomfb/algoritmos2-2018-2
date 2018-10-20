"""Classe Retângulo"""


class Retangulo:

    def __init__(self, x, y, w, h):
        self.posicao_x = x
        self.posicao_y = y
        self.largura = w
        self.altura = h
        self.cor = 0

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, self.cor, pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura))

    def troca_cor(self):
        import random
        cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255), (255, 165, 0,)]
        self.cor = random.choice(cores)
