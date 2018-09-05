from behave import given, when, then
from coordenadaRetangulo import teste

@given(u'um ponto com as coordenadas (7, 8)')
def coordenadas_ponto_true(context):
    """Dado as coordenadas do ponto"""
    context.ponto_cordenadaX =  7
    context.ponto_cordenadaY = 8

@given('um retângulo nas coordenadas (6,7) e dimensão (2,2)')
def coordenadas_retangulo_dimesao_true(context):
    """Dado as coordenadas do retângulo e a sua dimensão"""
    context.retangulo_coordenadaX = 6
    context.retangulo_coordenadaY = 7

    context.retangulo_dimencaoX_L = 2
    context.retangulo_dimencaoY_A = 2

@when('quero saber se o ponto está dentro do retangulo')
def testa_ponto_true(context):
    """Força o teste do ponto dentro do quadrado"""
    context.colidiu = teste(context.ponto_cordenadaX, context.ponto_cordenadaY, context.retangulo_coordenadaX, \
    context.retangulo_coordenadaY, context.retangulo_dimencaoX_L, context.retangulo_dimencaoY_A)

@then('o resultado é verdadeiro.')
def verifica_ponto_true(context):
    """Verifica se o resultado é verdadeiro"""
    assert (context.colidiu is True)

@given(u'um ponto com as coordenadas (5, 9)')
def coordenadas_ponto_false(context):
    """Dado as coordenadas do ponto"""
    context.ponto_cordenadaX =  5
    context.ponto_cordenadaY = 9

@given('um retângulo nas coordenadas (6,7) e dimensão (2,3)')
def coordenadas_retangulo_dimesao2_false(context):
    """Dado as coordenadas do retângulo e a sua dimensão"""
    context.retangulo_coordenadaX = 6
    context.retangulo_coordenadaY = 7

    context.retangulo_dimencaoX_L = 2
    context.retangulo_dimencaoY_A = 3

@then('o resultado é falso.')
def verifica_ponto_false(context):
    """Verifica se o resultado é false"""
    assert (context.colidiu is False)
