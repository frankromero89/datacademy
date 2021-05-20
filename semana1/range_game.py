def run():
    print('**Juego de rangos**')
    limite_1 = int(input('Ingresa el primer límite del rango: '))
    limite_2 = int(input('Ingresa el segundo limite del rango: '))
    comparador = int(input('Ingresa el número de comparación: '))
    
    my_range = None

    if limite_2 > limite_1:
        my_range = range(limite_1, limite_2)
    else: 
        my_range = range(limite_2, limite_1)

    is_in_range = comparador in my_range

    if is_in_range:
        print(f'Tu número es el {comparador} y se encuentra dentro del rango {limite_1} - {limite_2}')
    else:
        print('\n')
        print('\n')
        print(f'Tu número {comparador} no está dentro del rango')
        print('\n')
        print('\n')
        run()

if __name__ == '__main__':
    run()