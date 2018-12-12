# language: pt

Funcionalidade: Remover elementos da lista encadeada.

# Teste 1
Cenario: Remover elementos de uma lista existente.
    Dado que existe uma lista com os numeros [1, 2, 3, 1, 2, 3, 1, 2, 3]
    Quando eu removo os elementos com valor 3
    Entao a lista tem 6 elemento(s)
    E nenhum tem o valor 3
