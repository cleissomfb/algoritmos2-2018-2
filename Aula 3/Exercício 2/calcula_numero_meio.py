#Digitar três números e separa o númnero da esquerda, do meio e o da esquerda.

lista_num = [1, 2, 3]

def num_direita():
    direita_num = lista_num[0]
    for indice_direita in lista_num:
        if indice_direita > direita_num:
            direita_num = indice_direita
    return direita_num

def num_esqueda():
    esquerda_num = lista_num[0]
    for indice_esquerda in lista_num:
        if indice_esquerda < esquerda_num:
            esquerda_num = indice_esquerda
    return esquerda_num

def num_meio():
    direita_num = num_direita()
    esquerda_num = num_esqueda()
    i = 0
    meio_num = lista_num[0]
    while meio_num == direita_num or meio_num == esquerda_num:
        i += 1
        meio_num = lista_num[i]
    return meio_num

print ("Lista de números: ",str(lista_num).strip("[]"))
print ("Número da direita: ", num_direita())
print ("Número da esquerda: ", num_esqueda())
print ("Número do meio: ", num_meio())
