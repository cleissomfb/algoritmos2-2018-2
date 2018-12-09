"""Implementa os passos para testar a insercao em uma lista encadeada."""

from behave import given, then, when
from lista import ListaEncadeada


# Teste 1
@given('que existe uma lista vazia')
def _given_existe_uma_lista_vazia(context):
    context.lista = ListaEncadeada()


@when('eu adiciono o numero {numero:d} no final da lista')
def _when_adiciono_no_final_da_lista(context, numero):
    context.lista.append(numero)


@then('a lista tem {numero:d} elemento(s)')
def _then_lista_tem_N_elementos(context, numero):
    assert context.lista.size == numero


# Teste 2
@when('eu adiciono os numeros [{lista}] no final da lista')
def _when_adiciono_varios_numeros_no_final_da_lista(context, lista):
    for numero in lista.split(", "):
        context.lista.append(int(numero))


# Testes 3 e 4
@then('o primeiro elemento vale {numero:d}')
def _then_o_valor_do_primeiro_elemento(context, numero):
    assert numero == context.lista.first.value


@then('o ultimo elemento vale {numero:d}')
def _then_o_valor_do_ultimo_elemento(context, numero):
    assert numero == context.lista.last.value


# Teste 5
@given('que existe uma lista com os numeros [{lista}]')
def _given_existe_lista_com_elementos(context, lista):
    context.lista = ListaEncadeada()
    for numero in lista.split(", "):
        context.lista.append(int(numero))


# Teste 6
@when('eu adiciono o numero {numero:d} no inicio da lista')
def _when_adiciono_elemento_inicio_da_lista(context, numero):
    context.lista.addFirst(numero)


# Testes 7, 8 e 9
@when('eu adiciono os numeros [{lista}] no inicio da lista')
def _when_adiciono_varios_numeros_no_inicio_da_lista(context, lista):
    for numero in lista.split(", "):
        context.lista.addFirst(int(numero))
