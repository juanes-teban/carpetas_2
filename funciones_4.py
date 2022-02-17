'''
funciones_4.py
script en Python que implemente una función para calcular el área de un triángulo. Dicha función deberá recibir como argumentos el valor de la base y la altura y regresará el área calculada.
'''

def area_triangulo(altura, base):
    return base * altura / 2
print('Programa que calcula el área de un triangulo')
print('Ingresa los siguientes valores')
altura = float(input('Altura: '))
base = float(input('Base: '))

print(f'Área = {area_triangulo(altura,base):.2f}')



print('Nos vemos...')
