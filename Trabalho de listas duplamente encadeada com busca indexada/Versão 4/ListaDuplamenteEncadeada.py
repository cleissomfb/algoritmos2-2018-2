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
        self.indice = None

    def insert(self, valor):
        """Insere um valor ordenado na lista duplamente encadeada a partir do head."""
        if self.tail is None:
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
        self.indice = None

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
            self.indice = None

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

        def indice(self):
            """Cria um indice na lista encadeada para facilitar a procura."""
            if self.indice == None:
                self.indice = ListaDuplamenteEncadeada()
                self.indice.head = self.head
                ponteiro = self.head
                ponteiroIndice = self.indice.head

                while ponteiro is not None:
                    i = 0
                    while i < 5:
                        ponteiro = ponteiro.proximo
                        i += 1
                    novo_no = No(ponteiro)
                    self.indice.insert(novo_no)
                    if ponteiro == self.tail:
                        novo_no = No(ponteiro)
                        self.indice.insert(novo_no)



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

lista.removeValor(0)
lista.removeValor(3)
lista.removeValor(6)
lista.removeValor(9)
lista.removeValor(10)

lista.insert(6)

lista.imprimeListaDuplamenteEncadeada_crescente()
lista.imprimeListaDuplamenteEncadeada_decrescente()

print("\nO tamanho da lista é: ", lista.mostraTamanho())
