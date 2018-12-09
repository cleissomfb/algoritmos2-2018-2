# language: pt

Funcionalidade: Remover elementos da lista encadeada.

# Teste 10
Cenario: Remover elementos de uma lista existente.
    Dado que existe uma lista com os numeros [1, 2, 3, 1, 2, 3, 1, 2, 3]
    Quando eu removo os elementos com valor 3
    Entao a lista tem 6 elemento(s)
      E nenhum tem o valor 3

# Teste 11
Cenario: Remover elementos de uma lista vazia.
  Dado que existe uma lista vazia
  Quando eu removo os elementos com valor 3
  Entao a lista tem 0 elemento(s)

# Teste 12
Cenario: Remover o ultimo de uma lista vazia.
    Dado que existe uma lista vazia
    Quando eu removo o ultimo elemento
    Entao o elemento retornado e None
        E a lista tem 0 elemento(s)

# Teste 13
Cenario: Remover o ultimo de uma lista.
    Dado que existe uma lista com os numeros [1, 2, 3, 4]
    Quando eu removo o ultimo elemento
    Entao o elemento retornado tem o valor 4
        E a lista tem 3 elemento(s)
        E o ultimo valor e 3

# Teste 14
Cenario: Remover o ultimo de uma lista com um unico elemento.
    Dado que existe uma lista com os numeros [1]
    Quando eu removo o ultimo elemento
    Entao o elemento retornado tem o valor 1
        E a lista tem 0 elemento(s)

# Teste 15
Cenario: Remover o primeiro de uma lista vazia.
    Dado que existe uma lista vazia
    Quando eu removo o primeiro elemento
    Entao a lista tem 0 elemento(s)

# Teste 16
Cenario: Remover o primeiro de uma lista com um elemento.
    Dado que existe uma lista com os numeros [1]
    Quando eu removo o primeiro elemento
    Entao a lista tem 0 elemento(s)

# Teste 16
Cenario: Remover o primeiro de uma lista.
    Dado que existe uma lista com os numeros [1, 2, 3, 4]
    Quando eu removo o primeiro elemento
    Entao a lista tem 3 elemento(s)
        E o primeiro valor e 2
