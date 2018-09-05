from behave import given, when, then
from colisao_dois_retangulos import verifica_colisao

@given('dois retângulos nas coordenadas (6,7) (7,8) e dimensões (2,2) e (2,2)')
def coordenadas_retangulos1(context):
    """Dado as coordenadas e as dimensão dos retangulos para resultado true"""
    context.retangulo1_coordenadaX = 6
    context.retangulo1_coordenadaY = 7

    context.dimensaoX_retangulo1_L = 2
    context.dimensaoY_retangulo1_A = 2

    context.retangulo2_coordenadaX = 6
    context.retangulo2_coordenadaY = 7

    context.dimensaoX_retangulo2_L = 2
    context.dimensaoY_retangulo2_A = 2

@when('quero saber se os retângulos colidiram.')
def verificar_se_colidiram(context):
    """Quero verificer se eles colidiram"""
    context.colidiram = verifica_colisao(context.retangulo1_coordenadaX,\
     context.retangulo1_coordenadaY,context.dimensaoX_retangulo1_L,\
    context.dimensaoY_retangulo1_A,context.retangulo2_coordenadaX, context.dimensaoX_retangulo2_L,\
    context.dimensaoY_retangulo2_A)

@then('o resultado é verdadeiro.')
def verificacao_true(context):
    """Verifica se o resultado é verdadeiro"""
    assert (context.colidiram is True)

@given('dois retângulos nas coordenadas (6,7) (2,5) e dimensões (2,2) e (2,2)')
def coordenadas_retangulos2(context):
    """Dado as coordenadas e as dimensão dos retangulos para resultado false"""
    context.retangulo1_coordenadaX = 6
    context.retangulo1_coordenadaY = 7

    context.dimensaoX_retangulo1_L = 2
    context.dimensaoY_retangulo1_A = 2

    context.retangulo2_coordenadaX = 2
    context.retangulo2_coordenadaY = 2

    context.dimensaoX_retangulo2_L = 2
    context.dimensaoY_retangulo2_A = 2

@then('o resultado é falso.')
def verificacao_false(context):
    """Verifica se o resultado é falso"""
    assert (context.colidiram is False)
