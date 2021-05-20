import math

def area(base, altura):
    return (base * altura)/2

def calcular_tipo_de_triangulo(base, altura, angulo):
    ang_rad = math.radians(angulo)
    hipotenusa = altura / math.sin(ang_rad)
    print(f'hipotenusa: {hipotenusa}')
    media_base = round(base / 2, 2)
    first = (hipotenusa*hipotenusa) - (altura*altura)
    distancia_x = round(math.sqrt(first), 2)
    print(f'distancia_x: {distancia_x}')
    if distancia_x == base:
        return 'equilatero'
    if distancia_x == media_base:
        return 'isosceles'
    return 'escaleno'

def run():
    print('**Bienvenido a la calculadora de triangulos**')
    print('''Por favor ingresa la altura y base del triangulo para calcular el area.
    Si deseas conocer que tipo de tipo de triangulo es ingresa uno de los ángulos laterales del triangulo''')
    altura = float(input('Ingresa la altura del triangulo: '))
    base = float(input('Ingresa la base del triangulo: '))
    try:
        angulo = float(input('Ingresa la magnitud del ángulo de lo contrario solo presiona enter para conocer la base'))
    except:
        angulo = None
    print(angulo)
    area_triangulo = area(base,altura)
    print(area_triangulo)
    if angulo:
        tipo = calcular_tipo_de_triangulo(base, altura, angulo)
        print(tipo)

if __name__ == '__main__':
    run()
