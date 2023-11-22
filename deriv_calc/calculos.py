import sympy as sp

def calcular_derivada_raiz_quadrada(ponto):
    x = sp.symbols('x')
    funcao = sp.sqrt(x)
    derivada = sp.diff(funcao, x)
    valor_derivada = derivada.subs(x, ponto)
    return valor_derivada

def calcular_derivada_funcao_quadratica(ponto):
    x = sp.symbols('x')
    funcao = x**2 + 3*x + 2
    derivada = sp.diff(funcao, x)
    valor_derivada = derivada.subs(x, ponto)
    return valor_derivada

def calcular_derivada_logaritmo(ponto):
    x = sp.symbols('x')
    funcao = sp.log(x)
    derivada = sp.diff(funcao, x)
    valor_derivada = derivada.subs(x, ponto)
    return valor_derivada

def calcular_derivada_seno(ponto):
    x = sp.symbols('x')
    funcao = sp.sin(x)
    derivada = sp.diff(funcao, x)
    valor_derivada = derivada.subs(x, ponto)
    return valor_derivada

def calcular_derivada_cosseno(ponto):
    x = sp.symbols('x')
    funcao = sp.cos(x)
    derivada = sp.diff(funcao, x)
    valor_derivada = derivada.subs(x, ponto)
    return valor_derivada
