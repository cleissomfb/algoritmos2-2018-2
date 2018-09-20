"""Primreiro programa orientado a objeto"""
from estrelas import Estrela
import random

numero_estrelas = 20
lista_estrelas = []

coordenadaX = 0
coordenadaY = 0
velocidade = 0


def criar_estrelas(coordenadaX, coordenadaY, velocidade):
    coordenadaX = 800
    coordenadaY = random.randint(0, 600)
    velocidade = random.randint(1, 3)
    estrela = Estrela()
    estrela.set_coordenadaX(coordenadaX)
    estrela.set_coordenadaY(coordenadaY)
    estrela.set_velocidade(velocidade)
    return estrela


def cria_espaco():
    quantidade = 0
    lista_estrelas.append(criar_estrelas(coordenadaX, coordenadaY, velocidade))
    print("\nCria o espaço: ")
    print("X: ", lista_estrelas[quantidade].get_coordendaX())
    print("Y: ", lista_estrelas[quantidade].get_coordendaY())
    print("Velocidade: ", lista_estrelas[quantidade].get_velocidade())
    quantidade += 1


def move_estrelas():
    quantidade = 0
    lista_estrelas[quantidade].set_coordenadaX(lista_estrelas[quantidade].get_coordendaX() - lista_estrelas[quantidade].get_velocidade())
    print("\nMove a estrela da coordenadaX: ")
    print("X: ", lista_estrelas[quantidade].get_coordendaX())
    print("Y: ", lista_estrelas[quantidade].get_coordendaY())
    print("Velocidade: ", lista_estrelas[quantidade].get_velocidade())
    quantidade += 1


def criando_varias_estrelas():
    quantidade = 0
    while quantidade < numero_estrelas:
        lista_estrelas.append(criar_estrelas(coordenadaX, coordenadaY, velocidade))
        print("\nCria várias estrelas no espaço: ")
        print("X: ", lista_estrelas[quantidade].get_coordendaX())
        print("Y: ", lista_estrelas[quantidade].get_coordendaY())
        print("Velocidade: ", lista_estrelas[quantidade].get_velocidade())
        quantidade += 1


def move_varias_estrelas():
    quantidade = 0
    while quantidade < numero_estrelas:
        lista_estrelas[quantidade].set_coordenadaX(lista_estrelas[quantidade].get_coordendaX() - lista_estrelas[quantidade].get_velocidade())
        print("\nMove varias a estrela na coordenadaX: ")
        print("X: ", lista_estrelas[quantidade].get_coordendaX())
        print("Y: ", lista_estrelas[quantidade].get_coordendaY())
        print("Velocidade: ", lista_estrelas[quantidade].get_velocidade())
        quantidade += 1


criar_estrelas(coordenadaX, coordenadaY, velocidade)
cria_espaco()
move_estrelas()
criando_varias_estrelas()
move_varias_estrelas()
