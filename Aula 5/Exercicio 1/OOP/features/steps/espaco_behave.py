from behave import given, when, then
from espaco_cideral import criar_estrelas


@given('dois valores inteiros e positivos, 0 e 600')
def range_y(context):
    context.y_min = 0
    context.y_max = 600


@given('uma lista com os valores 1, 2 e 3')
def range_speed(context):
    context.speed_min = 1
    context.speed_max = 3


@when('eu crio um objeto que representa uma estrela')
def lista_estrela(context):
    context.espaco_cideral.criar_estrelas()


@then('a coordenada X da estrela é 800')
def coorX(context):
    assert(context.estrelas.set_coordenadaX() == 800)


@then('a coordenada Y da estrela esta entre 0 e 600')
def coorY(context):
    assert(context.set_coordenadaY() >= context.y_min and context.set_coordenadaY() <= context.y_max)


@then('a velocidade da estrela é 1, 2 ou 3')
def speed(context):
    assert(context.set_velocidade() >= context.speed_min and context.set_velocidade() <= context.speed_max)
