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

    def insert(self, valor):
        """Insere um valor ordenado na lista duplamente encadeada."""
        if self.tail is None:
            self.head = self.tail = No(valor)
            return
        inicio = self.head
        if valor < inicio.dado:
            print("Dado 1 if (Introduz no inicio)", inicio.dado)
            novo_dado = No(valor)
            novo_dado.proximo = inicio
            self.head = novo_dado
        else:
            while inicio is not None:
                dado_salvo = inicio.proximo
                if inicio == self.tail:
                    print("Dado 2 if (Introduz no final): ", inicio.dado)
                    novo_dado = No(valor)
                    inicio.proximo = novo_dado
                    inicio.anterior = inicio
                    self.tail = novo_dado
                    break
                elif valor < dado_salvo.dado:
                    print("Dado 2 elif (Introduz no meio): ", inicio.dado)
                    novo_dado = No(valor)
                    inicio.proximo = novo_dado
                    inicio.anterior = novo_dado.proximo
                    novo_dado.proximo = dado_salvo
                    novo_dado.anterio = inicio
                    break
                inicio = inicio.proximo

    def imprimeListaDuplamenteEncadeada(self):
        """Imprime a lista duplamente encadeada."""
        indice = self.head
        print("\n------ Itens adcionado a lista de forma ordenada -----")
        while indice is not None:
            print(indice.dado)
            indice = indice.proximo
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

lista.imprimeListaDuplamenteEncadeada()
