"""Implementa um a Pilha estatica."""


class StackUnderflow (Exception):
    """Define classede erro para acesso a pilhas vazias."""

    pass


class Pilha:
    """Implementa uma Pilha com tamanho estático."""

    def __init__(self, tamanho):
        """Inicializa um novo objeto pilha com  o tamanho estipulado."""
        self._dados = [0] * tamanho
        self._topo = 0

    def empty(self):
        """Verifica se a pilha esta vazia."""
        return self._topo == 0

    def push(self, valor):
        """Insere um valor na pilha."""
        self._dados[self._topo] = valor
        self._topo += 1

    def peek(self):
        """Retorna o valor que esta no topo da pilha."""
        if self.empty():
            raise StackUnderflow()
        return self._dados[self._topo - 1]
