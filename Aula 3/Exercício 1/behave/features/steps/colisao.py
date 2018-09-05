@given('um retângulo nas coordenadas (6,7) e dimensão (2,2)')
def coordenadas_dimesao(context):
    coordenadasX = 6
    coordenadasY = 7

    dimensaoX = 2
    dimensaoY = 2

@when('quero saber se o ponto está dentro do retangulo')
def step_impl(context):

@then('o resultado é verdadeiro.')
def step_impl(context):
    

@given('um ponto com as coordenadas (5, 9)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given um ponto com as coordenadas (5, 9)')

@given('um retângulo nas coordenadas (6,7) e dimensão (2,3)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given um retângulo nas coordenadas (6,7) e dimensão (2,3)')

@then('o resultado é falso.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o resultado é falso.')
