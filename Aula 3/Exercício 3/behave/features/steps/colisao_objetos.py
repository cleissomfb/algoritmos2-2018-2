from behave import given, when, then
from colisao_objetos import colisao_dois_retangulos

@given('dois retângulos nas coordenadas (6,7) (7,8) e dimensões (2,2) e (2,2)')
def coordenadas(context):
    retangulo1_coordenadaX = 6
    retangulo1_coordenadaY = 7

    dimensaoX_retangulo1_L = 2
    dimensaoY_retangulo1_A = 2

    retangulo2_coordenadaX = 7
    retangulo2_coordenadaY = 8

    dimensaoX_retangulo2_L = 2
    dimensaoY_retangulo2_A = 2

@when('quero saber se os retângulos colidiram.')
def verificacao(context):



@then('o resultado é verdadeiro.')
def status(context):


#@given('dois retângulos nas coordenadas (6,7) (2,5) e dimensões (2,2) e (2,2)')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Given dois retângulos nas coordenadas (6,7) (2,5) e dimensões (2,2) e (2,2)')

#@then('o resultado é falso.')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then o resultado é falso.')
