from factorial import func_factorial
from factorial2 import func_factorial2
import time
print('MENU')
print('a) primer algoritmo')
print('b) segundo algoritmo')
op = input('Teclea una opción: ')
if op == 'a':
    n = int(input("Teclea un número: "))
    func_factorial(n)
    print(func_factorial(n))

elif op == 'b':
    n = int(input("Teclea un número: "))
    func_factorial2(n)
    print(func_factorial2(n))
else:
    print('La opción tecleada es inválida.')
