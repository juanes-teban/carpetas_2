'''
funciones_1.py
script en Python que implemente una funcion para calcular el area de un triangulo
'''
def area_triangulo():
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    area = base * altura / 2
    return area

print('Programa para ca<lcular el area de un triangulo')
a = area_triangulo()
print(f'Area = {a}')

print('Nos vemos...')
