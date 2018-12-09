"""Comportamentos de um apilha."""

from behave import given, when, then

from pilha import Pilha, StackUnderflow


@given('o tamanho da pilha sendo {tam:d}')
def _given_tamanho_da_pilha(context, tam):
    context.tam = tam


@when('crio uma pilha')
def _when_crio_pilha(context):
    context.pilha = Pilha(context.tam)


@then('tenho uma pilha com capacidade {tam:d}')
def _then_tamanho_da_pilha(context, tam):
    assert tam == len(context.pilha._dados)


@then('a pilha esta vazia')
def _then_pilha_vazia(context):
    assert context.pilha.empty() is True


# Segundo cenario
@given('que eu tenho uma pilha')
def _given_uma_pilha(context):
    context.pilha = Pilha(10)


@when('insiro o valor {valor:d}')
def _when_push_um_valor(context, valor):
    context.pilha.push(valor)


@then('a pilha nao esta vazia')
def _then_pilha_nao_vazia(context):
    assert context.pilha.empty() is False


@then('o topo da pilha tem o valor {valor:d}')
def _then_topo_tem_valor_especifico(context, valor):
    assert valor == context.pilha.peek()


# Terceiro cenario
@when('consulto o topo da pilha')
def _when_consulto_topo_piulha(context):
    try:
        context.result = context.pilha.peek()
        context.exception = None
    except Exception as e:
        context.exception = e


@then('uma excecao StackUnderflow e gerada')
def _then_excao_stack_underflow(context):
    assert context.exception is not None
    assert isinstance(context.exception, StackUnderflow) is True
