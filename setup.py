from setuptools import setup

setup(
    name='deriv-calculus',
    version='0.1',
    packages=['deriv_calc'],
    install_requires=[
        # Dependências do pacote
        'sympy'
    ],
    entry_points={
        'console_scripts': [
            'calc_deriv=script:calc_deriv',
        ],
    },
    # Metadados
    author='Charlie C.',
    author_email='charliesamoel@gmail.com',
    description='Esse pacote serve para calculo de derivadas',
    url='https://github.com/CharlieCidral/deriv-pypck',
)
