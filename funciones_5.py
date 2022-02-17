'''
funciones_5.py
script en Python que implemente una función que haga el cálculo del IMC del usuario. La función debe recibir el peso y la estatura del usuario y como resultado regresa el valor índice de masa corporal.
'''
def calculador_IMC(peso, estatura):
    return peso / (estatura ** 2)

print('Programa que calcula el IMC')
print('Ingresa los siguientes datos')
p = float(input('Peso: '))
e = float(input('Estatura: '))

print(f'IMC = {calculador_IMC(p,e):.2f} ')

print('Nos vemos...')
