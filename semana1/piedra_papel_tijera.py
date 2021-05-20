import inquirer
import random
from inquirer.themes import GreenPassion
from os import kill

def game():
    print('Vamos a jugar: "Piedra, papel o tijeras"')
    pc_select = random.choice(['piedra', 'papel', 'tijeras'])
    question = [
        inquirer.List('eleccion',
            message="Priedra, papel o tijeras?",
            choices=['piedra', 'papel', 'tijeras'],
        ),
    ]
    player_select = inquirer.prompt(question, theme=GreenPassion())

    return (player_select['eleccion'], pc_select)

def run(player_scr = 0, pc_scr = 0):
    player_score = player_scr
    pc_score = pc_scr

    while player_score < 3 and pc_score < 3:
        player_select, pc_select = game()
        print(player_select)
        print(f'pc eligío: {pc_select}')

        if player_select == pc_select:
            print('\n')
            run(player_score, pc_score)
        elif player_select == "piedra" and pc_select == "tijeras":
            player_score += 1
            print(f'Ganaste, llevas {player_score} partidas ganadas')
            print('\n')
        elif player_select == "tijeras" and pc_select == "papel":
            player_score += 1
            print(f'Ganaste, llevas {player_score} partidas ganadas')
            print('\n')
        elif player_select == "papel" and pc_select == "piedra":
            player_score += 1
            print(f'Ganaste, llevas {player_score} partidas ganadas')
            print('\n')
        else:
            pc_score += 1
            print(f'Perdiste, llevas {pc_score} partidas perdidas')
            print('\n')

    if player_score > pc_score:
        print(f'FELECIDADES GANASTE EL 2 DE 3!!!!')
    else:
        print(f'LO SENTIMOS PERDISTE EL 2 DE 3, SUERTE LA PROXIMA :(')
    exit()


if __name__ == '__main__':
    run()