import sympy as sp

# Defina o símbolo
x = sp.symbols('x')

def regra_constante():
    return sp.diff(7, x)

def regra_poder():
    return sp.diff(x**5, x)

def regra_soma():
    return sp.diff(x**2 + x**3, x)

def regra_diferenca():
    return sp.diff(x**2 - x**3, x)

def regra_produto():
    return sp.diff((x**2)*(x**3), x)

def regra_quociente():
    return sp.diff((x**2)/(x**3), x)

def regra_cadeia():
    return sp.diff(sp.sin(x**2), x)

def funcao_exponencial():
    return sp.diff(sp.exp(x), x)

def funcao_logaritmica():
    return sp.diff(sp.log(x), x)

def funcao_trigonometrica_seno():
    return sp.diff(sp.sin(x), x)

def funcao_trigonometrica_cosseno():
    return sp.diff(sp.cos(x), x)
