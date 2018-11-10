"""Lista encadeada simples ordenada."""


class No:
    """Define um nó em um lista encadeada simples."""

    def __init__(self, valor):
        """Inicializa Nó."""
        self.dado = valor
        self.proximo = None


class ListaEncadeada:
    """Define a lista encadeada."""

    def __init__(self):
        """Inicializa a lista encadeada."""
        self.head = None
        self.tail = None

    def append(self, valor):
        """Adiciona um valor na lista."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo

    def insert(self, valor):
        """Insere um valor ordenado na lista."""
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
                    self.tail = novo_dado
                    break
                elif valor < dado_salvo.dado:
                    print("Dado 2 elif (Introduz no meio): ", inicio.dado)
                    print("Dado_salvo: ", dado_salvo.dado)
                    novo_dado = No(valor)
                    inicio.proximo = novo_dado
                    novo_dado.proximo = dado_salvo
                    break
                inicio = inicio.proximo


lista = ListaEncadeada()
lista.append(6)
lista.append(8)
lista.append(17)
lista.append(23)

lista.insert(5)
lista.insert(10)
lista.insert(20)
lista.insert(22)
lista.insert(25)

i = lista.head
while i is not None:
    print(i.dado)
    i = i.proximo

print("Esse e o Head depois do Insert: ", lista.head.dado)
print("Esse e o Tail depois do Insert: ", lista.tail.dado)
