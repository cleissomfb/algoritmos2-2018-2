"""Implementa os passos para testar a insercao em uma lista."""

from behave import given, then, when
from TrabalhoListaDuplamenteEncadeada import ListaDuplamenteEncadeada

# Teste 1


@given('que existe uma lista vazia')
def given_existe_uma_lista_vazia(context):
    context.lista = ListaDuplamenteEncadeada()


@when('eu adiciono o numero {numero:d} no final da lista')
def when_adiciono_no_final(context, numero):
    context.lista.insert(numero)


@then('a lista tem {numero:d} elemento(s)')
def then_lista_tem_n_elementos(context, numero):
    assert context.lista.mostraTamanho() == numero

# Teste 2


@when('eu adiciono os numeros [{lista}] no final da lista')
def when_quando_eu_add_uma_lista(context, lista):
    for numero in lista.split(", "):
        context.lista.insert(int(numero))

# Teste 3 e 4


@then('o primeiro elemento vale {numero:d}')
def then_o_valor_do_primeiro_elemento(context, numero):
    assert numero == context.lista.primeiroElemento().dado


@then('o ultimo elemento vale {numero:d}')
def then_o_valor_do_ultimo_elemento_teste3(context, numero):
    assert numero == context.lista.ultimoElemento().dado


@then('o ultimo elemento vale {numero:d}')
def then_o_valor_ultimo_elemento_teste4(context, numero):
    assert numero == context.lista.ultimoElemento().dado


# Teste 5

@given('que existe uma lista com os numeros [{lista}]')
def then_existe_uma_lista_com_elementos(context, lista):
    context.lista = ListaDuplamenteEncadeada()
    for numero in lista.split(", "):
        context.lista.insert(int(numero))
