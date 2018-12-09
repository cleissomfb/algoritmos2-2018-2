"""Pergunta 1 - Prova N2"""


class Fila:
    """Implementa uma fila de tamanho estatico"""

    def __init__(self):
        """Inicializa a fila."""
        self.dados = []
        self.tamanho = 0

    def push(self, valor):
        """Insere um valor na estrutura."""
        self.dados.append(valor)
        self.tamanho += 1

    def pop(self):
        """Retira um valor da estrutura."""
        if not self.empty():
            self.tamanho -= 1
            primeiroRetirar = self.dados.pop(0)
            return primeiroRetirar

    def peek(self):
        """Mostra o próximo valor a ser retirado."""
        valorRetirar = self.dados[self.tamanho - self.tamanhoFila()]
        return valorRetirar

    def empty(self):
        """Verifica se a estrutura está vazia."""
        return self.tamanhoFila() == 0

    def imprimeFila(self):
        """Imprime a fila."""
        i = 0
        while i < len(self.dados):
            print(self.dados[i])
            i += 1

    def inverteFila(self):
        """Inverte a fila."""
        i = len(self.dados) - 1
        print("--------------------")
        print("Fila Invertida: ")
        while i >= 0:
            print(self.dados[i])
            i -= 1

    def tamanhoFila(self):
        """Retorna o tamanho da fila."""
        return self.tamanho


fila = Fila()
fila.push(1)
fila.push(2)
fila.push(3)
fila.push(4)
fila.push(5)
fila.push(6)

print("\nLista inicial: ", fila.dados)
print("Tamanho Inicial: ", fila.tamanho)

fila.pop()
print("\nImpressão após do pop:")
fila.imprimeFila()
print("Tamanho da lista: ", fila.tamanho)

fila.peek()
print("\nProximo valor a ser retirado: ", fila.peek())
print("\nImpressão após do peek:")
fila.imprimeFila()

fila.inverteFila()
