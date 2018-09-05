#Objetivo: Verificar se houve colisão entre dois retangulos.

#Usuario digita a coordenada do primeiro retangulo.
retangulo1_coordenadaX = int(input ("Digite a coordenada X do primeiro retângulo: "))
retangulo1_coordenadaY = int(input ("Digite a coordenada Y do primeiro retângulo: "))

#Usuario digita a coordenada do primeiro retangulo.
dimensaoX_retangulo1_L = int(input ("Digite a dimenção X do primeiro retângulo: "))
dimensaoY_retangulo1_A = int(input ("Digite a dimenção Y do primeiro retângulo: "))

#Usuario digita a coordenada do segundo retangulo.
retangulo2_coordenadaX = int(input ("Digite a coordenada X do segundo retângulo: "))
retangulo2_coordenadaY = int(input ("Digite a coordenada Y do segundo retângulo: "))

#Usuario digita a dimensão do segundo retangulo.
dimensaoX_retangulo2_L = int(input ("Digite a dimenção X do segundo retângulo: "))
dimensaoY_retangulo2_A = int(input ("Digite a dimenção Y do segundo retângulo: "))

#Teste para saber se o programa estava funcionando.
#retangulo1_coordenadaX = 6
#retangulo1_coordenadaY = 7

#dimensaoX_retangulo1_L = 2
#dimensaoY_retangulo1_A = 2

#retangulo2_coordenadaX = 6
#retangulo2_coordenadaY = 7

#dimensaoX_retangulo2_L = 2
#dimensaoY_retangulo2_A = 2

#O if está fazendo o teste para verificar se o primriro retangulo digitado pelo
#usuario está colidindo com o segundo retangulo digitado pelo usuario.
if ((retangulo1_coordenadaX + dimensaoX_retangulo1_L > retangulo2_coordenadaX) and
    (retangulo1_coordenadaX < retangulo2_coordenadaX + dimensaoX_retangulo2_L) and
    (retangulo1_coordenadaY + dimensaoY_retangulo1_A > retangulo2_coordenadaY) and
    (retangulo1_coordenadaY < retangulo2_coordenadaY + dimensaoY_retangulo2_A)):
    #Se os retangulos colidiram, informa na tela: Os retangulos colidiram!
    print ("Os retangulos colidiram!")
else:
    #Se os retangulos não colidiram, informa na tela: Os retangulos não colidiram!
    print ("Os retangulos não colidiram!")
