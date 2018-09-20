
import random

lista_estrelas = []

x = 0
y = []
velocidade = []


def cria_array_coordenadaX():
    x = [800]
    return x


def cria_array_coordenadaY():
    y.append(random.randint(0, 600))
    return y


def cria_array_velocidade():
    velocidade.append(random.randint(1, 3))
    return velocidade


def une_tudo():
    coorX = cria_array_coordenadaX()
    coorY = cria_array_coordenadaY()
    vel = cria_array_velocidade()

    return coorX, coorY, vel


def cria_estrelas():
    lista_estrelas.append(une_tudo())
    return lista_estrelas


#def move_estrelas():
#    lista_estrelas
#    return lista_estrelas


cria_estrelas()
print(cria_estrelas())
print(move_estrelas())
