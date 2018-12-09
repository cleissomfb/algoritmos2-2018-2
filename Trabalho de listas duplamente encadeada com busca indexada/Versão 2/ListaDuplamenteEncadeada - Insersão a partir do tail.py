"""Trabalho sobre Listas duplamente encadeada com procura indexada."""


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

    def insert(self, valor):
        """Insere um valor ordenado na lista duplamente encadeada a partir do head."""
        if self.tail is None:
            self.head = self.tail = No(valor)
            self.tamanho += 1
            return
        inicio = self.head
        if valor < inicio.dado:
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
                elif valor < dado_salvo.dado:
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


lista = ListaDuplamenteEncadeada()
lista.insert(3)
lista.insert(8)
lista.insert(0)
lista.insert(10)
lista.insert(5)
lista.insert(6)
lista.insert(9)
lista.insert(1)
lista.insert(4)
lista.insert(2)
lista.insert(7)


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

lista.imprimeListaDuplamenteEncadeada_crescente()
lista.imprimeListaDuplamenteEncadeada_decrescente()
print("\nO tamanho da lista é: ", lista.mostraTamanho())
