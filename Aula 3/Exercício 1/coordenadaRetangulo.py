#Objetivo: Verificar se um ponto está dentro de um retangulo.

#Usuario digita a posição do ponto.
#ponto_cordenadaX = int(input ("Digite a coordenada X do ponto: "))
#ponto_cordenadaY = int(input ("Digite a coordenada Y do ponto: "))

#Usuario digita as coordenada do retangulo.
#retangulo_coordenadaX = int(input ("Digite a coordenada X do retângulo: "))
#retangulo_coordenadaY = int(input ("Digite a coordenada Y do retângulo: "))

#Usuario digita a dimenção do triangulo.
#retangulo_dimencaoX_L = int(input ("Digite a dimenção X do retângulo: "))
#retangulo_dimencaoY_A = int(input ("Digite a dimenção Y do retângulo: "))

#Teste para saber se o programa estava funcionando.
ponto_cordenadaX = 7
ponto_cordenadaY = 8

retangulo_coordenadaX = 6
retangulo_coordenadaY = 7

retangulo_dimencaoX_L = 2
retangulo_dimencaoY_A = 2

#O if está testando se o ponto está dentro do retangulo.
def teste(ponto_cordenadaX, ponto_cordenadaY, retangulo_coordenadaX, retangulo_coordenadaY, \
    retangulo_dimencaoX_L, retangulo_dimencaoY_A):
    if ((retangulo_coordenadaX + retangulo_dimencaoX_L > ponto_cordenadaX) and
        (retangulo_coordenadaX < ponto_cordenadaX) and
        (retangulo_coordenadaY + retangulo_dimencaoY_A > ponto_cordenadaY) and
        (retangulo_coordenadaX < ponto_cordenadaY)) :
        #Se o ponto estiver dentro do retangulo, informa na tela: O ponto está dentro do retângulo.
        print ("\nO ponto está dentro do retângulo.")
        return True
    else:
        #Se o ponto não estiver dentro do retangulo, informa na tela: O ponto não está dentro do retângulo.
        print ("\nO ponto não está dentro do retângulo.")
        return False

teste(ponto_cordenadaX, ponto_cordenadaY, retangulo_coordenadaX, retangulo_coordenadaY, retangulo_dimencaoX_L, retangulo_dimencaoY_A)
