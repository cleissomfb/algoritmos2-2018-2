"""Comparativos de uma fila circular."""

from behave import given, when, then

from Pergunta2 import FilaCircular

#Cenario 1


@given('o tamanho da estrutura sendo {tam:d}')
def tamanho_estrutura(context, tam):
    context.tam = tam


@when('crio um deque')
def crio_um_duque(context):
    context.filacircular = FilaCircular(context.tam)


@then('tenho um deque com capacidade para armazenar {tam:d} elementos')
def tenho_um_duque_com_capacidade_10(context, tam):
    assert tam == len(context.filacircular.elementos)


@then('a estrutura esta vazia')
def estrutura_esta_vazia(context):
    assert context.filacircular.empty() is True


#Cenario2


@given('que eu tenho um deque')
def tenho_um_duque(context):
    context.filacircular = FilaCircular(10)


@when('insiro, no final da estrutura, o valor {valor:d}')
def insiro_final_da_escrita(context, valor):
    context.filacircular.pushBack(valor)


@then('a estrutura nao esta vazia')
def estrutura_nao_esta_vazia(context):
    assert context.filacircular.empty() is False


@then('o elemento na frente da estrutura tem o valor {valor:d}')
def o_elemento_frente_e_8(context, valor):
    assert valor == context.filacircular.peekFront()

#Cenario3


@when('insiro, no final da estrutura, os valores [1, 2, 3, 4]')
def insiro_final_da_estrutura(context):
    context.filacircular.pushBack(1)
    context.filacircular.pushBack(2)
    context.filacircular.pushBack(3)
    context.filacircular.pushBack(4)


@then('o elemento no final da estrutura tem o valor {valor:d}')
def elemento_final_4(context, valor):
    assert valor == context.filacircular.peekBack()

# Cenario4


@given('este deque tem os elementos, inseridos no final, [1, 3, 5, 7]')
def valores_inseridos_fianl(context):
    context.filacircular.pushBack(1)
    context.filacircular.pushBack(3)
    context.filacircular.pushBack(5)
    context.filacircular.pushBack(7)
