# language: pt

Funcionalidade: Criar uma pilha com tamanho estático.

Cenario: Criar uma pilha.
  Dado o tamanho da pilha sendo 10
  Quando crio uma pilha
  Entao tenho uma pilha com capacidade 10
    E a pilha esta vazia

Cenario: Inserir um valor na pilha.
  Dado que eu tenho uma pilha
  Quando insiro o valor 8
  Entao a pilha nao esta vazia
    E o topo da pilha tem o valor 8

Cenario: Acessar um valor de uma pilha vazia
  Dado que eu tenho uma pilha
  Quando consulto o topo da pilha
  Entao uma excecao StackUnderflow e gerada
