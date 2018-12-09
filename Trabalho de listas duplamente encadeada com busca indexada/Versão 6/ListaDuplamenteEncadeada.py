"""Trabalho sobre Listas duplamente encadeada com procura indexada."""
import random


class No:
    """Define um nó em uma lista duplamente encadeada."""

    def __init__(self, valor):
        """Inicializa o Nó."""
        self.dado = valor
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    """Define a lista encadeada."""

    def __init__(self):
        """Inicializa a lista encadeada."""
        self.head = None
        self.tail = None
        self.tamanho = 0
        self.indice = None

    def insert(self, valor):
        """Insere um valor ordenado na lista duplamente encadeada a partir do head."""
        self.indice = None #Torna o indice none
        if self.head is None: #Testa se há valores adicionados no nó
            self.head = self.tail = No(valor)
            self.tamanho += 1
            return
        inicio = self.head
        if valor <= inicio.dado: #Insere no inicio
            # print("Dado 1 if (Introduz no inicio)", inicio.dado)
            novo_dado = No(valor)
            novo_dado.proximo = inicio
            novo_dado.anterior = None
            inicio.anterior = novo_dado
            inicio = novo_dado
            self.head = novo_dado
            self.tamanho += 1
        else:
            while inicio is not None:
                dado_salvo = inicio.proximo
                if inicio == self.tail: #Insere no fim
                    # print("Dado 2 if (Introduz no final): ", inicio.dado)
                    novo_dado = No(valor)
                    novo_dado.proximo = None
                    novo_dado.anterior = self.tail
                    self.tail.proximo = novo_dado
                    self.tail = novo_dado
                    self.tamanho += 1
                    break
                elif valor <= dado_salvo.dado: #Insere no meio
                    # print("Dado 2 elif (Introduz no meio): ", inicio.dado)
                    novo_dado = No(valor)
                    self.proximo = inicio.proximo
                    inicio.proximo = novo_dado
                    novo_dado.anterior = inicio
                    self.proximo.anterior = novo_dado
                    novo_dado.proximo = self.proximo
                    self.tamanho += 1
                    break
                inicio = inicio.proximo

    def insertApartirDoTail(self, valor):
        """Insere de forma ordenada na lista duplamente encadeada a partir do tail."""
        if self.head is None:
            self.head = self.tail = No(valor)
            self.tamanho += 1
            return
        final = self.tail
        if valor >= final.dado:
            # print("Dado 1 if (Introduz no final)", final.dado)
            novo_dado = No(valor)
            novo_dado.proximo = None
            novo_dado.anterior = self.tail
            self.tail.proximo = novo_dado
            self.tail = novo_dado
            self.tamanho += 1
        else:
            while final is not None:
                dado_salvo = final.anterior
                if final == self.head:
                    # print("Dado 2 if (Introduz no inicio): ", final.dado)
                    novo_dado = No(valor)
                    novo_dado.proximo = final
                    novo_dado.anterior = None
                    final.anterior = novo_dado
                    final = novo_dado
                    self.head = novo_dado
                    self.tamanho += 1
                    break
                elif valor >= dado_salvo.dado:
                    # print("Dado 2 elif (Introduz no meio): ", final.dado)
                    novo_dado = No(valor)
                    self.anterior = final.anterior
                    final.anterior = novo_dado
                    novo_dado.proximo = final
                    self.anterior.proximo = novo_dado
                    novo_dado.anterior = self.anterior
                    self.tamanho += 1
                    break
                final = final.anterior

    def removeValor(self, valor):
        """Remove um valor da lista duplamente encadeada, se ele existir."""
        remove = self.pesquisaValores(valor)
        inicio = self.head
        if inicio is None:
            return None
        while inicio is not None:
            self.indice = None
            if inicio.dado == valor:
                if inicio.anterior is None: #Remove no inicio
                    self.head = inicio.proximo
                    inicio.proximo.anterior = None
                    self.tamanho -= 1
                elif inicio == self.tail: #Remove no fim
                    self.tail = self.tail.anterior
                    self.tail.proximo = None
                    inicio = self.tail.anterior
                    self.tamanho -= 1
                else: #Remove no meio
                    inicio.anterior.proximo = inicio.proximo
                    inicio.proximo.anterior = inicio.anterior
                    self.tamanho -= 1
                print("Valor removido: ", remove.dado)
            inicio = inicio.proximo

    def mostraTamanho(self):
        """Mostra o tamanho atual da lista duplamente encadeadas."""
        return self.tamanho

    def imprimeListaDuplamenteEncadeada_crescente(self):
        """Imprime a lista duplamente encadeada."""
        indice = self.head
        print("\n------ Itens adcionado a lista de forma ordenada -----")
        print("Vizualização de forma crescente:\n")
        while indice is not None:
            print(indice.dado)
            indice = indice.proximo
        print("\nO head é: ", self.head.dado)
        print("O tail é: ", self.tail.dado)

    def imprimeListaDuplamenteEncadeada_decrescente(self):
        """Imprime a lista duplamente encadeada."""
        indice = self.tail
        print("\n------ Itens adcionado a lista de forma ordenada -----")
        print("Vizualização de forma decrescente:\n")
        while indice is not None:
            print(indice.dado)
            indice = indice.anterior
        print("\nO head é: ", self.head.dado)
        print("O tail é: ", self.tail.dado)

    def criaIndice(self):
        """Cria um indice na lista encadeada para facilitar a procura."""
        # print("\n------------- Criando a lista de Indices ------------------\n")
        lista_obj = self.head #Adiciona o head em uma variavel
        x = 0
        while x < 10: #Verifica se está pulando de 10 em 10
            i = 0
            while i < 10: #Verifica se esta pulando de 1 em 1
                if lista_obj.proximo is not None:
                    # print("Passou para o proximo obj: ", lista_obj.dado)
                    lista_obj = lista_obj.proximo
                else:
                    break #Achou o numero
                i += 1
            self.insereValoresIndice(lista_obj) #Adicionou o num na lista de indices
            x += 1

    def insereValoresIndice(self, valor):
        """Insere valores para ter o indice."""
        if self.indice is None: #Verifica se a lista de indices está vazia
            self.indice = ListaDuplamenteEncadeada()
        indice_lista = self.indice #Adiciona o indice em uma variavel
        no_indice = No(valor) #Cria um novo nó
        if indice_lista.head is None: #Testa se o head do indice é none
            # print("Introduz antes do indice ser none")
            indice_lista.head = no_indice
            indice_lista.tail = indice_lista.head
        else: #Adiciona os indices no tail da lista
            # indice = indice_lista.tail
            # print("Introduz após o indice ser none: ", indice.dado.dado)
            no_indice.anterior = indice_lista.tail
            no_indice.proximo = None
            indice_lista.tail.proximo = no_indice
            indice_lista.tail = no_indice

    def pesquisaValores(self, valor):
        """Pesquisa os valores na lista duplamente encadeada."""
        self.criaIndice()  # Cria a lista de indices
        indiceIndex = self.indice.head  # Coloca o head da lista de indices em uma variavel
        # print("\nValor do indice: ", indiceIndex.dado.dado)
        while indiceIndex is not None:  # Testa se a lista de indices não e none
            indiceLista = indiceIndex.dado  # Adiciona o .dado da lista de indice em uma variavel
            if not(valor >= self.head.dado and valor <= self.tail.dado):  # Testa se o .dado esta na lista duplamente encadiada
                print("\nO valor não está na lista.")
                return None
            elif indiceLista.dado >= valor:  # Testa se o valor e maior que o .dado da lista de indices
                # print("\nIndice maior encontrado: ", indiceLista.dado)
                while indiceLista.dado > valor:  # Testa se o .dado da lista de indices e maior que o valor
                    indiceLista = indiceLista.anterior # Se não e maior ele volta um no e testa novamente
                    # print("Diminuindo o indice: ", indiceLista.dado)
                # print("Indice real encontrado: ", indiceLista.dado)
                if indiceLista.dado == valor:  # Testa se o .dado e igual ao valor
                    return indiceLista
                else:
                    print("\nO valor não está na lista.")
                    return None
                break
            indiceIndex = indiceIndex.proximo  # Passa para o proximo valor contido no indice

    def insereValores(self, quantidade):
        """Insere valores de forma randomica."""
        # for i in range(quantidade):
        #     num_random = random.randint(0, 100)
        #     self.insert(num_random)
        i = 0
        while i <= quantidade:
            num_random = random.randint(0, 100)
            # self.insert(num_random)
            self.insertApartirDoTail(num_random)
            i += 1

    def insertValoresOrdenadas(self, quantidade):
        """Insere valores de de 1 a 'quantidade' de forma ordenada."""
        # for i in range(quantidade):
        #     self.insert(i)
        i = 0
        while i <= quantidade:
            self.insert(i)
            # self.insertApartirDoTail(i)
            i += 1

    def imprimir_indice(self):
        """Impressao utilizada para imprimir o dado do dado do indice."""
        indice = self.head
        while indice is not None:
            print(indice.dado.dado)
            indice = indice.proximo

    def primeiroElemento(self):
        """Retorna o primeiro elemento da lista."""
        return self.head

    def ultimoElemento(self):
        """Retorna o ultímo elemento da lista."""
        return self.tail


lista = ListaDuplamenteEncadeada()

# lista.insereValores(100)
lista.insertValoresOrdenadas(100)

print("\n------------ Valores contidos na lista -------------\n")
print("Primeiro valor da lista: ", lista.primeiroElemento().dado)
print("Ultimo valor da lista: ", lista.ultimoElemento().dado)

# Inserindo novos valores à lista.
lista.insert(130)
lista.insert(120)
lista.insert(110)

print("\n------------ Novos valores contidos na lista -------------\n")
print("Primeiro valor da lista: ", lista.primeiroElemento().dado)
print("Ultimo valor da lista: ", lista.ultimoElemento().dado)

print("\n-------------  Remoção de valores -------------\n")
lista.removeValor(10)
lista.removeValor(25)
lista.removeValor(50)
lista.removeValor(70)
lista.removeValor(100)

# lista.insert(6)
# lista.criaIndice()

# lista.imprimeListaDuplamenteEncadeada_crescente()
# lista.imprimeListaDuplamenteEncadeada_decrescente()

print("\n------------- Tamanho da Lista -------------")
print("\nO tamanho da lista é: ", lista.mostraTamanho())

print("\n------------ Pesquisa de indices -------------")
indice1 = lista.pesquisaValores(67)
if indice1 is not None:
    print("\nO dado foi encontrado na lista: ", indice1.dado)

print("\n------------ Número dos Indices --------------")
indice = lista.indice
print("\nPrimeiro indice: ", indice.primeiroElemento().dado.dado)
print("Ultímo Indice: ", indice.ultimoElemento().dado.dado, "\n")
indice.imprimir_indice()
