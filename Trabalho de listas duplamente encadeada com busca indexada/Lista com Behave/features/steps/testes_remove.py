"""Testes de remoção de elementos da Lista Duplamente Encadeada."""

from behave import then, when


# Teste 1
@when('eu removo os elementos com valor {numero:d}')
def when_remove_elementos_com_um_valor_especifico(context, numero):
    """Quando eu removo N valores."""
    context.lista.removeValor(numero)


@then('nenhum tem o valor {numero:d}')
def then_nenhum_valor_equivalente(context, numero):
    """Nenhum tem N valor."""
    iterador = context.lista.primeiroElemento()
    while iterador is not None:
        assert numero != iterador.dado
        iterador = iterador.proximo
