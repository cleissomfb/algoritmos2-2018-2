# language: pt

Funcionalidade: Adicionar elementos a lista encadeada.

# Teste 1
Cenario: Adicionar um elemento no final da lista.
    Dado que existe uma lista vazia
    Quando eu adiciono o numero 5 no final da lista
    Entao a lista tem 1 elemento(s)

# Teste 2
Cenario: Adicionar dois elementos no final da lista.
    Dado que existe uma lista vazia
    Quando eu adiciono os numeros [1, 2] no final da lista
    Entao a lista tem 2 elemento(s)

# Teste 3
Cenario: Adicionar dois elementos no final da lista, verificando os valores.
    Dado que existe uma lista vazia
    Quando eu adiciono os numeros [1, 2] no final da lista
    Entao o primeiro elemento vale 1
      E o ultimo elemento vale 2

# Teste 4
Cenario: Adicionar varios elementos no final da lista.
    Dado que existe uma lista vazia
    Quando eu adiciono os numeros [1, 2, 5, 3] no final da lista
    Entao a lista tem 4 elemento(s)
      E o primeiro elemento vale 1
      E o ultimo elemento vale 3

# Teste 5
Cenario: Adicionar um elemento no final de uma lista existente.
    Dado que existe uma lista com os numeros [1, 2, 5, 3]
    Quando eu adiciono o numero 8 no final da lista
    Entao a lista tem 5 elemento(s)
      E o primeiro elemento vale 1
      E o ultimo elemento vale 8

# Teste 6
Cenario: Adicionar um elemento no inicio de uma lista vazia.
    Dado que existe uma lista vazia
    Quando eu adiciono o numero 3 no inicio da lista
    Entao a lista tem 1 elemento(s)

# Teste 7
Cenario: Adicionar varios elementos no inicio de uma lista vazia.
    Dado que existe uma lista vazia
    Quando eu adiciono os numeros [1, 2, 5, 3] no inicio da lista
    Entao a lista tem 4 elemento(s)

# Teste 8
Cenario: Adicionar dois elementos no final da lista.
    Dado que existe uma lista com os numeros [1, 2, 5, 3]
    Quando eu adiciono o numero 4 no inicio da lista
    Entao a lista tem 5 elemento(s)
      E o primeiro elemento vale 4
      E o ultimo elemento vale 3

# Teste 9
Cenario: Adicionar dois elementos no final da lista.
    Dado que existe uma lista com os numeros [1, 2, 5, 3]
    Quando eu adiciono os numeros [4, 3] no inicio da lista
    Entao a lista tem 6 elemento(s)
      E o primeiro elemento vale 3
      E o ultimo elemento vale 3
