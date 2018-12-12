"""Testes de pesquisa para Lista Duplamente Encadeada."""
from behave import given, then, when
from TrabalhoListaDuplamenteEncadeada import ListaDuplamenteEncadeada


# Teste 1
@given('que exista uma lista com os numeros [{lista}]')
def given_existe_uma_lista(context, lista):
    """Quando existe uma lista de numeros."""
    context.lista = ListaDuplamenteEncadeada()
    for numero in lista.split(", "):
        context.lista.insert(int(numero))


@when('eu pesquiso pelo numero {numero:d}')
def when_eu_pesquiso(context, numero):
    """Eu pesquiso pelo N valor."""
    context.lista.pesquisaValores(numero)


@then('a pesquisa me retorna o numero {numero:d}')
def then_a_lista_retorna_o_valor(context, numero):
    """Eu pesquiso e me retorna N Valor."""
    assert numero == context.lista.pesquisaValores(numero).dado


# Teste 2
@then('a pesquisa me retorna que nao tem o numero {numero:d} na lista')
def then_a_pesquisa_retorna_que_o_numero_nao_existe_na_lista(context, numero):
    """Eu pesquiso e me retorna um valor inexistente na lista."""
    assert numero != context.lista.pesquisaValores(numero)
