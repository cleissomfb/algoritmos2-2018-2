"""Cria a classe estrela"""


class Bola:

    def __init__(self):
        self.centro_x = 0
        self.centro_y = 0
        self.raio = 0
        self.cor = 0

    def set_centro_x(self, coordenadaX):
            self.centro_x = coordenadaX

    def set_centro_y(self, coordenadaY):
            self.centro_y = coordenadaY

    def set_raio(self, raio):
        self.raio = raio

    def get_centro_x(self):
        return self.centro_x

    def get_centro_y(self):
        return self.centro_y

    def get_raio(self):
        return self.raio

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, self.cor, [self.centro_x, self.centro_y], self.raio)

    def move(self, dx, dy):
        x = self.centro_x
        y = self.centro_y
        self.centro_x = x + dx
        self.centro_y = y + dy

    def troca_cor(self):
        import random
        cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        self.cor = random.choice(cores)
