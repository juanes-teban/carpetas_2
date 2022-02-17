'''
funciones_3.py
script en Python que implemente una función encargada de convertir grados Fahrenheit a Celsius.
'''
def fahrenheit_a_celcius():
    f = float(input('Grados Fahrenheit'))
    c = (f-32)/1.8
    return c
print('Programa que convierte grados Fahrenheit a celcius')
celcius = fahrenheit_a_celcius()
print(f'Celcius: {celcius :.2f}')

print('Nos vemos...')
