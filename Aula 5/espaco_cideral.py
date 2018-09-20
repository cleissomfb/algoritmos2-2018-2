#from estrelas import Estrela
import random

numero_estrelas = 5
estrelas = []


#def criarEspaco():
#    coordenadaX = 800
#    coordenadaY = random.randint(0,600)
#    velocidade = random.randint(1,3)

#    estrela = Estrela()
#    estrela.set_coordenadaX(coordenadaX)
#    estrela.set_coordenadaY(coordenadaY)
#    estrela.set_velocidade(velocidade)

#    return estrela

#def menu_principal():
#    quantidade = 0
#    while quantidade < numero_estrelas:
#        estrelas.append(criarEspaco())
#        print ("==========")
#        print (estrelas[quantidade].get_coordendaX())
#        print (estrelas[quantidade].get_coordendaY())
#        print (estrelas[quantidade].get_velocidade())
#        quantidade += 1

#menu_principal()

def menu_principal():
    quantidade = 0
    while quantidade < numero_estrelas:
        x = 800
        y = random.randint(0,600)
        velocidade = random.randint(1,3)

        teste = x, y, velocidade

        estrelas.append(teste)

        print("==========")
        print(estrelas[quantidade])
        quantidade += 1

menu_principal()
