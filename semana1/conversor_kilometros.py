import inquirer
from inquirer.themes import GreenPassion

def run():
    mile_in_km = 1.609344
    question = [
        inquirer.List('convert',
            message="Priedra, papel o tijeras?",
            choices=['km a millas', 'millas a kilometros'],
        ),
    ]
    convertion = inquirer.prompt(question, theme=GreenPassion())

    if convertion["convert"] == "km a millas":
        meassure = float(input('Ingresa los kilometros a convertir: '))
        print(f"{meassure} kilometros equivale a: {round(meassure/mile_in_km, 3)} millas")
    else:
        meassure = float(input('Ingresa las millas a convertir: '))
        print(f"{meassure} millas equivale a: {round(meassure * mile_in_km, 3)} kilometros")



if __name__ == '__main__':
    run()