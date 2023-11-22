# Cálculo de Derivadas

Este pacote Python fornece funções para calcular as derivadas de várias funções comuns.

## Instalação

Para instalar este pacote, navegue até o diretório que contém o `setup.py` e execute o seguinte comando:

```
pip install deriv-calculus

```

# Uso

Depois de instalar o pacote, você pode importar as funções de cálculo de derivadas em seus scripts. Aqui está um exemplo:
```
from deriv_calc.calculos import calcular_derivada_funcao_quadratica

# Agora você pode usar a função para calcular a derivada de uma função quadrática
derivada = calcular_derivada_funcao_quadratica(2)
print(f"A derivada da função quadrática no ponto 2 é: {derivada}")
```

# Funções Disponíveis
O pacote inclui as seguintes funções para calcular derivadas:

- calcular_derivada_raiz_quadrada(ponto)
- calcular_derivada_funcao_quadratica(ponto)
- calcular_derivada_logaritmo(ponto)
- calcular_derivada_seno(ponto)
- calcular_derivada_cosseno(ponto)
Cada função calcula a derivada de uma função específica no ponto especificado.

# Testes
Para executar os testes unitários para este pacote, você pode usar o seguinte comando:
```
python -m unittest test_calc.py

```
# Contribuindo
Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar um Pull Request ou abrir uma Issue.

# Licença
Este projeto está licenciado sob os termos da licença MIT.
