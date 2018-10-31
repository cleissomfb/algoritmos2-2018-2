"""Exercicio de Lista Encadeada."""


class No:
    """Define um no da lista encadeada."""

    def __init__(self, valor):
        """Inicializa no."""
        self.dado = valor
        self.proximo = None


class ListaEncadeada:
    """Define lista encadeada."""

    def __init__(self):
        """Inicializa uma nova lista."""
        self.head = None
        self.tail = None
        self.tamanho = 0

    def append(self, valor):
        """Adiciona um valor ao final da lista."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo
        self.tamanho += 1

    def addFirst(self, novo_dado):
        """Adciona um novo valor na cabeça da lista."""
        novo_dado = No(novo_dado)
        novo_dado.proximo = self.head
        self.head = novo_dado
        self.tamanho += 1

    def removeFirst(self):
        """Remove o primeiro elemento da tabela."""
        self.head = self.head.proximo
        self.tamanho -= 1

    def first(self):
        """Mostra o primeiro elemento da lista encadeada."""
        return self.head

    def last(self):
        """Mostra o ultimo elemento da lista encadeada."""
        return self.tail

    def size(self):
        """Mostra o tamanho total da lista encadeada."""
        return self.tamanho

    def remove(self, valor):
        """Remove todos os elementos que forem igual ao valor informado."""
        inicio = self.head
        anterior = None
        while inicio.proximo is not None:
            anterior = inicio
            inicio = inicio.proximo
            if inicio.dado == valor:
                anterior.proximo = inicio.proximo
                inicio = anterior
                self.tamanho -= 1

    def pop(self):
        """remove o elemento no final da lista e o retorna ao chamador."""
        if self.head is None:
            return None
        if self.head == self.tail:
            pop = self.head
            self.head = self.tail = None
            self.tamanho -= 1
            return pop
        cabeca = self.head
        while cabeca.proximo is not None:
            if cabeca.proximo == self.tail:
                pop = cabeca
                self.tail = cabeca
            cabeca = cabeca.proximo
        self.tamanho -= 1

        return pop


x = ListaEncadeada()
x.append(1)
x.append(7)
x.append(3)
x.append(3)
x.append(7)

x.addFirst(7)
x.removeFirst()
x.remove(3)

i = x.head
while i is not None:
    print(i.dado)
    i = i.proximo
print("Valor do POP: ", x.pop().dado)
print("O primeiro elemento da lista: ", x.first().dado)
print("O ultimo elemento da lista: ", x.last().dado)
print("O tamanho total da lista: ", x.size())
