"""Implementa os passos para testar a remocao de uma lista encadeada."""

from behave import then, when


# Testes 10 e 11
@when('eu removo os elementos com valor {numero:d}')
def _when_remove_elementos_com_um_valor_especifico(context, numero):
    context.lista.remove(numero)


@then('nenhum tem o valor {numero:d}')
def _then_nenhum_valor_equivalente(context, numero):
    iterador = context.lista.first
    while iterador is not None:
        assert numero != iterador.value
        iterador = iterador.next


# Teste 12
@when('eu removo o ultimo elemento')
def _when_removo_ultimo_elemento(context):
    context.result = context.lista.pop()


@then('o elemento retornado e None')
def _then_ultimo_elemento_none(context):
    assert context.result is None


# Teste 13
@then('o ultimo valor e {valor:d}')
def _then_ultimo_valor(context, valor):
    last = context.lista.last.value
    assert valor == last


# Testes 13 e 14
@then('o elemento retornado tem o valor {valor:d}')
def _then_elemento_retornado_tem_valor(context, valor):
    assert context.result == valor


# Testes 15 e 16
@when('eu removo o primeiro elemento')
def _when_removo_primeiro_elemento(context):
    context.lista.removeFirst()


# Teste 17
@then('o primeiro valor e {valor:d}')
def _then_primeiro_valor(context, valor):
    first = context.lista.first.value
    assert valor == first
