#Digitar três números e separa o númnero da esquerda, do meio e o da esquerda.

#Usuário digita uma sequencia de trÊs números.
numeros = int(input ("\nDigite uma sequencia de três números: "))

#Faz a divisão por 100 para pegar o número da direita que representa a centena.
num_Direita = numeros // 100
#Faz o nódulo de 100 para descobrir quais são as dezenas.
num_Meio = numeros % 100
#Faz a divisão da váriavel num_Meio para ficar apenas com a dezena.
num_Meio_Aux = num_Meio // 10
#Faz o módulo de 10 para pegar o número da esquerda que representa a unidade.
num_Esquerda = numeros % 10

#Imprime o número digitado.
print ("\nNumero digitado: ", numeros)
#Imprimi o número da direita.
print ("Número da direita: ", num_Direita)
#Imprime o número do meio.
print ("Número do meio: ", num_Meio_Aux)
#Imprime o número da esquerda.
print ("Número da esquerda: ", num_Esquerda)
