# language: pt

Funcionalidade: Pesquisar elementos na lista encadeada.

# Teste 1
Cenario: Pesquisar numero que está na lista.
    Dado que exista uma lista com os numeros [1, 2, 3, 4, 5]
    Quando eu pesquiso pelo numero 3
    Entao a pesquisa me retorna o numero 3

# Teste 2
Cenario: Pesquisar numero que não está na lista.
    Dado que exista uma lista com os numeros [1, 2, 3, 4, 5]
    Quando eu pesquiso pelo numero 6
    Entao a pesquisa me retorna que nao tem o numero 6 na lista
