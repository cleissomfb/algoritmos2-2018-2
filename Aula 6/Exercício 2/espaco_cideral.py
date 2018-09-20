#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Primreiro programa orientado a objeto"""

#Classe Estrelas
from estrelas import Estrela

#Módulos
import random
import pygame
from pygame.locals import *

"""Numeros de estrelas que será gerado"""
numero_estrelas = 35

"""Lista que será armanezado as estrelas"""
lista_estrelas = []

"""Variaveis da altura e da largura da tela"""
width = 640
height = 480

"""Definição de cores do cenário"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

"""Métodos de geração e criação das estrelas"""
def criar_estrelas(param): #Método que gera as estrelas as estrelas
    if param == 1:
        coordenadaX = 800
    elif param == 2:
        coordenadaX = random.randint(0, 800)
    coordenadaY = random.randint(0, 600)
    velocidade = random.randint(1, 3)

    estrela = Estrela()

    estrela.set_coordenadaX(coordenadaX)
    estrela.set_coordenadaY(coordenadaY)
    estrela.set_velocidade(velocidade)

    return estrela


def criando_varias_estrelas(): #Método que adiciona as estrelas a lista de estrelas
    quantidade = 0
    while quantidade < numero_estrelas:
        lista_estrelas.append(criar_estrelas(2))
        quantidade += 1

"""Inicio da contrução do jogo usando o módulo Pygame"""
def main(): #Método principal
    screen = pygame.display.set_mode((width, height)) #Cria a tela
    pygame.display.set_caption("Espaço Cideral") #Adiciona um nome na tela

    rodando = True

    criar_estrelas(1) #Inicia a construção das estrelas
    criando_varias_estrelas() #Armazena as estrelas geradas no "criar_estrelas" na lista de estrelas

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Cria o evento de fechar o game utilizando o "x" no canto superior direito
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: #Encerra o jogo ao clicar o botão "ESC" do teclado
                if event.key == pygame.K_ESCAPE:
                    rodando = False

        quantidade = 0

        pygame.draw.rect(screen, BLACK, [0, 0, 800, 600], ) # Cria o blackground preto

        while quantidade < numero_estrelas: # Gera a movimentação das estrelas
            lista_estrelas[quantidade].set_coordenadaX(lista_estrelas[quantidade].get_coordendaX() - lista_estrelas[quantidade].get_velocidade())
            pygame.draw.rect(screen, WHITE, [lista_estrelas[quantidade].get_coordendaX(), lista_estrelas[quantidade].get_coordendaY(), lista_estrelas[quantidade].get_velocidade(), lista_estrelas[quantidade].get_velocidade()], ) #Gera os retangulos brancos que parecem estrelas

            if lista_estrelas[quantidade].get_coordendaX() <= 0: #Cria a movimentação das estrelas da direita para a esquerda
                lista_estrelas[quantidade] = criar_estrelas(1)

            pygame.display.flip() #	Atualize a superfície de exibição completa para a tela

            quantidade += 1


if __name__ == '__main__':
    pygame.init()
    main()
