import inquirer
from inquirer.themes import GreenPassion
import math

def cilindro_vol(radio, altura):
    return round((math.pi * (radio**2) * altura), 3)


def cubo_vol(lado):
    return round(lado**3, 3)


def esfera_vol(radio):
    return round(((4/3*math.pi) * radio**3), 3)

def run():
    print('***Calculadora de volumenes***')
    question = [
            inquirer.List('figura',
                message="De que figura te gustaría calcular el volumen?",
                choices=['cilindro', 'esfera', 'cubo'],
            ),
        ]
    figura = inquirer.prompt(question, theme=GreenPassion())

    if figura['figura'] == 'cilindro':
        radio = float(input('Por favor ingresa el radio de uno de los extremos del cilindro: '))
        altura = float(input('Por favor ingresa la altura del cilindro: '))
        volumen = cilindro_vol(radio, altura)
        print(f'El volumen es: {volumen}')

    if figura['figura'] == 'cubo':
        lado = float(input('Por favor ingresa la medida de cualquiera de los lados: '))
        volumen = cubo_vol(lado)
        print(f'El volumen es: {volumen}')

    if figura['figura'] == 'esfera':
        radio = float(input('Por favor ingresa el radio de la esfera: '))
        volumen = esfera_vol(radio)
        print(f'El volumen es: {volumen}')


if __name__ == '__main__':
    run()