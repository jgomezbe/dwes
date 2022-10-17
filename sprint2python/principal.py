from factorial import func_factorial
from factorial2 import func_factorial2
import time
print('MENU')
print('a) primer algoritmo')
print('b) segundo algoritmo')
op = input('Teclea una opción: ')
if op == 'a':
    start_time = time.time()
    n = int(input("Teclea un número: "))
    func_factorial(n)
    print(func_factorial(n))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')

elif op == 'b':
    start_time = time.time()
    n = int(input("Teclea un número: "))
    func_factorial2(n)
    end_time = time.time()
    elapsed_time = end_time-start_time
    print(func_factorial2(n))
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
else:
    print('La opción tecleada es inválida.')
