"""Implementa os passos para testar a remocao de uma lista encadeada."""

from behave import then, when

# Teste 6


@when('eu removo os elementos com valor {numero:d}')
def when_remove_elementos_com_um_valor_especifico(context, numero):
    context.lista.removeValor(numero)


@then('nenhum tem o valor {numero:d}')
def then_nenhum_valor_equivalente(context, numero):
    iterador = context.lista.primeiroElemento()
    while iterador is not None:
        assert numero != iterador.dado
        iterador = iterador.proximo
