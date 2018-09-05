import sys
num_array = []

def menu_principal(): #Menu principal do programa
    print ("\n1 - Digitar uma lista de números")
    print ("2 - Visualizar a lista de números")
    print ("3 - Vizualizar maior número e seu indice da lista")
    print ("4 - Vizualizar menor número e seu indice da lista")
    print ("5 - Vizualizar a soma dos números pares")
    print ("6 - Vizualizar a soma dos números impares")
    print ("7 - Vizualizar a soma da divisão dos números de indice par pelos de indice impar")
    print ("8 - Vizualizar a lista na ordem inversa")
    print ("0 - Sair do programa")

    try: #Faz o teste para ver se foi digitado alguma letra
        item_menu = (int(input("\nDigite uma opção do menu: ")))
    except Exception as e:
        print ("\nSomente números, tente novamente!\n")
        menu_principal()

    if (item_menu == 0): #Testa a opcão '0' do menu princial
        print ("\nDeseja sair do programa?")
        print ("1 - Sim")
        print ("2 - Não")

        try: #Faz o teste para ver se foi digitado alguma letra
            item_menu_sair = (int(input("\nDigite a opção do menu: ")))
        except Exception as e:
            print ("\nSomente números, tente novamente!\n")
            menu_principal()

        if (item_menu_sair == 1):
            print ("\nProgama fechado.")
            sys.exit()#Fecha o programa
        elif (item_menu_sair == 2):
            print("\nOpção de saída do programa foi cancelada!")
            menu_principal()
        else:
            print ("\nMenu inválido, tente novamente!")
            menu_principal()
    elif (item_menu == 1): #Testa a opcão '1' do menu princial
        digitacao_array_num()
        menu_principal()
    elif (item_menu == 2): #Testa a opcão '2' do menu princial
        print ("\nA lista original é: ", str(num_array).strip("[]"))
        menu_principal()
    elif (item_menu == 3): #Testa a opcão '3' do menu princial
        print ("\nO número maior é ", valor_maior() , "e o seu indice é: ", indice_maior())
        menu_principal()
    elif (item_menu == 4): #Testa a opcão '4' do menu princial
        print ("\nO número menor é ", valor_menor() , "e o seu indice é: ", indice_menor())
        menu_principal()
    elif (item_menu == 5): #Testa a opcão '5' do menu princial
        print ("\nA soma dos números pares é:", soma_pares())
        menu_principal()
    elif (item_menu == 6): #Testa a opcão '6' do menu princial
        print ("\nA soma dos números impares é: ", soma_impares())
        menu_principal()
    elif (item_menu == 7): #Testa a opcão '7' do menu princial
        print ("A soma da divisão dos indices impares pelos indices pares é: ", divisao_indice_par_impar())
        menu_principal()
    elif (item_menu == 8): #Testa a opcão '8' do menu princial
        print ("\nA impressão inversa do array é: ", str(impressao_inversa_array()).strip("[]"))
        menu_principal()
    else:
        print("\nMenu inválido, tente novamente!")
        menu_principal()

def digitacao_array_num():#Metodo para fazer a digitação de valores ára o array
    indice = 0
    encerra = 0
    if indice == len(num_array):
        for i in range(5):
            print ("\nLista de números do array: [Digite '0' para encerrar a digitação]", indice+1,":10")
            try:
                encerra = (int(input("Digite um número: ")))
            except Exception as e:
                print ("\nSomente números, tente novamente!\n")
                digitacao_array_num()
            indice += 1
            if encerra == 0:
                print ("\nDigitação cancelada.")
                num_array.clear()
                menu_principal()
            else:
                num_array.append(encerra)
    else:
        print("\nLista cheia\n")

    #while indice < 10:                         |
    #num = int(input("Digite um número: "))     |   Outra opção de fazer o metodo de digitação repetir
    #indice += 1                                |
    #num_array.append(num)                      |

def valor_maior(): #Método para verificar o maior valor contido no array.
    #iMaior = max(num_array) | Outra opção mais simples para ver o maior valor contido no array.
    iMaior = num_array[0]
    for valor_maior in num_array:
        if valor_maior > iMaior:
            iMaior = valor_maior
    return iMaior

def valor_menor(): #Método para verificar o menor valor contido no array.
    #iMenor = min(num_array) | Outra opção mais simples para ver o menor valor contido no array.
    iMenor = num_array[0]
    for valor_menor in num_array:
        if valor_menor < iMenor:
            iMenor = valor_menor
    return iMenor

def indice_maior(): # Método para verificar em qual posição do array está o maior valor do array.
    indice_Maior = 0
    for indice_maior in range(len(num_array)):
        if valor_maior() == num_array[indice_maior]:
            indice_Maior = indice_maior
    return indice_Maior

def indice_menor(): # Método para verificar em qual posição do array está o menor valor do array.
    indice_Menor = 0
    for indice_menor in range(len(num_array)):
        if valor_menor() == num_array[indice_menor]:
            indice_Menor = indice_menor
    return indice_Menor

def soma_pares(): # Método para verificar qual a soma de todos os números pares que estão no array
    soma_num_pares = 0
    for indice_soma_pares in num_array:
        if indice_soma_pares % 2 == 0:
            soma_num_pares += indice_soma_pares
    return soma_num_pares

def soma_impares(): # Método para verificar qual a soma de todos os números impares que estão no array
    soma_num_impares = 0
    for indice_soma_impares in num_array:
        if indice_soma_impares % 2 == 1:
            soma_num_impares += indice_soma_impares
    return soma_num_impares

def divisao_indice_par_impar(): #Método que soma todos os números pares com todos os números impares
    soma_indice_par_impar = 0
    soma_indice_par_impar = soma_pares() + soma_impares()
    return soma_indice_par_impar

def impressao_inversa_array(): # Método utilizado para inverter o array

    #array_aux = [num_array[-i] for i in range(1, len(num_array) + 1)] | Outra forma para fazer a inverção do array

    #inicio = 0                                                             |
    #fim = len(num_array) - 1                                               |
    #while inicio < fim:                                                    | Outra forma para fazer a inverção do array
    #num_array[inicio], num_array[fim] = num_array[fim], num_array[inicio]  |
    #inicio += 1                                                            |
    #fim -= 1                                                               |

    array_aux = num_array[::-1] # Forma mais simples para inverter o array
    return array_aux

print ("\nLista de Arrays\n")

menu_principal() #Inicia o programa
