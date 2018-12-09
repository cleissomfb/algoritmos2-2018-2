"""Classe Rebatedor"""


class Rebatedor:

    def __init__(self, x, y, w, h):
        self.posicao_x = x
        self.posicao_y = y
        self.largura = w
        self.altura = h

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura))

    def move_cima(self, height):
        self.posicao_y -= 5
        if self.posicao_y <= 0:
            self.posicao_y = 0

    def move_baixo(self):
        self.posicao_y += 5
        if self.posicao_y >= 380:
            self.posicao_y = 380

    def move_direta(self, width):
        self.posicao_x += 5
        if self.posicao_x + self.largura > width:
            self.posicao_x = width - self.largura

    def move_esquerda(self):
        self.posicao_x -= 5
        if self.posicao_x < 0:
            self.posicao_x = 0
