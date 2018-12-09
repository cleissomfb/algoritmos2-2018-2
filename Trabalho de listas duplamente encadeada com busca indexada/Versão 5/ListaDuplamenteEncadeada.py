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
        self.indice = None
        if self.head is None:
            self.head = self.tail = No(valor)
            self.tamanho += 1
            return
        inicio = self.head
        if valor <= inicio.dado:
            print("Dado 1 if (Introduz no inicio)", inicio.dado)
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
                if inicio == self.tail:
                    print("Dado 2 if (Introduz no final): ", inicio.dado)
                    novo_dado = No(valor)
                    novo_dado.proximo = None
                    novo_dado.anterior = self.tail
                    self.tail.proximo = novo_dado
                    self.tail = novo_dado
                    self.tamanho += 1
                    break
                elif valor <= dado_salvo.dado:
                    print("Dado 2 elif (Introduz no meio): ", inicio.dado)
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
            print("Dado 1 if (Introduz no final)", final.dado)
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
                    print("Dado 2 if (Introduz no inicio): ", final.dado)
                    novo_dado = No(valor)
                    novo_dado.proximo = final
                    novo_dado.anterior = None
                    final.anterior = novo_dado
                    final = novo_dado
                    self.head = novo_dado
                    self.tamanho += 1
                    break
                elif valor >= dado_salvo.dado:
                    print("Dado 2 elif (Introduz no meio): ", final.dado)
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
        """Remove um valor da lista duplamente encadeada."""
        self.indice = None

        inicio = self.head
        if inicio is None:
            return None
        while inicio is not None:
            if inicio.dado == valor:
                if inicio.anterior is None:
                    self.head = inicio.proximo
                    inicio.proximo.anterior = None
                    self.tamanho -= 1
                elif inicio == self.tail:
                    self.tail = self.tail.anterior
                    self.tail.proximo = None
                    inicio = self.tail.anterior
                    self.tamanho -= 1
                else:
                    inicio.anterior.proximo = inicio.proximo
                    inicio.proximo.anterior = inicio.anterior
                    self.tamanho -= 1
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
        lista_obj = self.head
        x = 0
        while x < 10:
            i = 0
            while i < 10:
                if lista_obj.proximo is not None:
                    print("Passou para o proximo obj: ", lista_obj.dado)
                    lista_obj = lista_obj.proximo
                else:
                    break
                i += 1
            self.insereValoresIndice(lista_obj)
            x += 1

    def insereValoresIndice(self, valor):
        """Insere valores para ter o indice."""
        if self.indice is None:
            self.indice = ListaDuplamenteEncadeada()
        indice_lista = self.indice
        no_indice = No(valor)
        if indice_lista.head is None:
            print("Introduz antes do indice ser none")
            indice_lista.head = no_indice
            indice_lista.tail = indice_lista.head
        else:
            print("Introduz após o indice ser none: ", indice_lista)
            no_indice.anterior = indice_lista.tail
            no_indice.proximo = None
            indice_lista.tail.proximo = no_indice
            indice_lista.tail = no_indice

    def pesquisaValores(self, valor):
        """Pesquisa os valores na lista duplamente encadeada."""
        self.criaIndice()
        indiceIndex = self.indice.head
        while indiceIndex is not None:
            indiceLista = indiceIndex.dado
            if not(valor >= self.head.dado and valor <= self.tail.dado):
                print("O valor não está na lista.")
                return None
            elif indiceLista.dado >= valor:
                print("Indice encontrado: ", indiceLista.dado)
                while indiceLista.dado > valor:
                    indiceLista = indiceLista.anterior
                # print("O valor do while é: ", indiceLista.dado)
                if indiceLista.dado == valor:
                    return indiceLista
                else:
                    print("O valor não está na lista.")
                    return None
                break
        indiceIndex = indiceIndex.proximo

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
        i = 1
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


lista = ListaDuplamenteEncadeada()

# lista.insereValores(100)
lista.insertValoresOrdenadas(100)
# lista.insert(3)
# lista.insert(8)
# lista.insert(0)
# lista.insert(10)
# lista.insert(5)
# lista.insert(6)
# lista.insert(9)
# lista.insert(1)
# lista.insert(4)
# lista.insert(2)
# lista.insert(7)


# lista.insertApartirDoTail(3)
# lista.insertApartirDoTail(8)
# lista.insertApartirDoTail(0)
# lista.insertApartirDoTail(10)
# lista.insertApartirDoTail(5)
# lista.insertApartirDoTail(6)
# lista.insertApartirDoTail(9)
# lista.insertApartirDoTail(1)
# lista.insertApartirDoTail(4)
# lista.insertApartirDoTail(2)
# lista.insertApartirDoTail(7)

# lista.removeValor(10)
# lista.removeValor(25)
# lista.removeValor(50)
# lista.removeValor(70)
# lista.removeValor(100)

# lista.insert(6)
lista.criaIndice()
# lista.pesquisaValores(41)

# lista.imprimeListaDuplamenteEncadeada_crescente()
# lista.imprimeListaDuplamenteEncadeada_decrescente()

print("\nO tamanho da lista é: ", lista.mostraTamanho())

print("\n------- Indices ---------")
index = lista.indice
index.imprimir_indice()
