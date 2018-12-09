"""Pergunta 2 - Prova N2"""


class FilaCircular:

    def __init__(self, tamanho):
        """Inicializa a fila curcular."""
        self.elementos = [0] * tamanho
        self.inicio = 0
        self.fim = 0
        self.tamanho_lista = 0

    def empty(self):
        """Testa se a fila circular esta vazia."""
        return self.lista_tamanho() == 0

    def lista_tamanho(self):
        """Retorna o tamanho da lista circular."""
        return self.tamanho_lista

    def pushBack(self, valor):
        """inserção no fim."""
        self.elementos[self.fim] = valor
        self.fim += 1
        self.tamanho_lista += 1

    def peekFront(self):
        """O método de consulta do elemento na frente da estrutura."""
        return self.elementos[self.lista_tamanho() - self.lista_tamanho()]

    def peekBack(self):
        """O método de consulta do elemento no final da estrutura."""
        return self.elementos[self.lista_tamanho() - 1]

    def full(self):
        """O método de verificação para saber se a estrutura está cheia."""
        return lista_tamanho() == 10
