"""Exercicio sobre a lista encadeada - Aula 11."""


class No:
    """Define um no da lista encadeada."""

    def __init__(self, valor):
        """Inicializa no."""
        self.dado = valor
        self.proximo = None


class Lista:
    """Define lista encadeada."""

    def __init__(self):
        """Inicializa uma nova lista."""
        self.head = None
        self.tail = None

    def append(self, valor):
        """Adiciona um valor ao final da lista."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo

    def addFirst(self, novo_dado):
        """Adciona um novo valor na cabeça da lista."""
        novo_dado = No(novo_dado)
        novo_dado.proximo = self.head
        self.head = novo_dado

    def removeFirst(self):
        """Remove o primeiro valor da lista encadeada."""
        self.head = self.head.proximo

    def removeLast(self):
        """Remove o ultimo valor da lista encadeada."""
        cabeca = self.head
        anterior = None

        if self.head.proximo is None:
            self.head = None
            self.proximo = None
        else:
            while cabeca.proximo is not None:
                anterior = cabeca
                cabeca = cabeca.proximo
                if cabeca.proximo is None:
                    anterior.proximo = None
                    self.tail = anterior


x = Lista()
x.append(1)
x.append(2)
x.append(3)
x.addFirst(4)
x.addFirst(5)
x.removeFirst()
x.removeLast()
i = x.head
while i is not None:
    print(i.dado)
    i = i.proximo
