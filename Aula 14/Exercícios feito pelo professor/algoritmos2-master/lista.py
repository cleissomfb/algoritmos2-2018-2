"""Implementa a estrutura de dados Lista Encadeada."""


class ListaEncadeada:
    """Implementa uma estrutura de dados do tipo Lista Encadeada."""

    class No:
        """Implementa um No (Elo) de uma lista encadeada."""

        def __init__(self, value):
            """
            Inicia um novo No, com o valor dado.

            Parameters
            ----------
            value: O valor a ser armazenado.

            """
            self._value = value
            self.next = None

        @property
        def value(self):
            """Retorna o valor do no."""
            return self._value

    def __init__(self):
        """Inicializa um novo objeto ListaEncadeada."""
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """
        Insere um valor no final da lista.

        Parameters
        ----------
        value: O valor a ser adicionado.

        """
        if self.tail is None:
            self.head = self.tail = ListaEncadeada.No(value)
        else:
            self.tail.next = ListaEncadeada.No(value)
            self.tail = self.tail.next
        self._size += 1

    def addFirst(self, value):
        """
        Insere um valor no final da lista.

        Parameters
        ----------
        value: O valor a ser adicionado.

        """
        novo = ListaEncadeada.No(value)
        if self.head is None:
            self.tail = novo
        else:
            novo.next = self.head
        self.head = novo
        self._size += 1

    def remove(self, valor):
        """
        Remove todos os elementos de uma lista com um valor especifico.

        Parameters
        ----------
        value: O valor a ser removido.

        """
        while self.head is not None and self.head.value == valor:
            self.head = self.head.next
            self._size -= 1
        if self.head is not None:
            last = self.head
            i = self.head.next
            while i is not None:
                if i.value == valor:
                    last.next = i.next
                    self._size -= 1
                else:
                    last = i
                i = i.next
            else:
                self.tail = last
        else:
            self.tail = None

    def pop(self):
        """Remove o ultimo elemento da lista e o retorna."""
        if self.tail is None:
            return None
        value = self.tail.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            iterator = self.head
            while iterator.next is not self.tail:
                iterator = iterator.next
            iterator.next = None
            self.tail = iterator
        self._size -= 1
        return value

    def removeFirst(self):
        """Remove o primeiro elemento da lista."""
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self._size -= 1

    @property
    def size(self):
        """Retorna o numero de elementos armazenados na lista."""
        return self._size

    @property
    def first(self):
        """Retorna o primeiro elemento da lista."""
        return self.head

    @property
    def last(self):
        """Retorna o ultimo elemento da lista."""
        return self.tail
