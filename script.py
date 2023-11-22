from deriv_calc.calculos import (
    calcular_derivada_raiz_quadrada,
    calcular_derivada_funcao_quadratica,
    calcular_derivada_logaritmo,
    calcular_derivada_seno,
    calcular_derivada_cosseno,
)

def calc_deriv():
    ponto_exemplo = 2

    resultado_raiz_quadrada = calcular_derivada_raiz_quadrada(ponto_exemplo)
    print(f'A derivada da raiz quadrada é: {resultado_raiz_quadrada}')

    resultado_funcao_quadratica = calcular_derivada_funcao_quadratica(ponto_exemplo)
    print(f'A derivada da função quadrática é: {resultado_funcao_quadratica}')

    resultado_logaritmo = calcular_derivada_logaritmo(ponto_exemplo)
    print(f'A derivada do logaritmo é: {resultado_logaritmo}')

    resultado_seno = calcular_derivada_seno(ponto_exemplo)
    print(f'A derivada do seno é: {resultado_seno}')

    resultado_cosseno = calcular_derivada_cosseno(ponto_exemplo)
    print(f'A derivada do cosseno é: {resultado_cosseno}')

if __name__ == "__main__":
    calc_deriv()
