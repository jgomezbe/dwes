from factorial import func_factorial

print('MENU')
print('a) primer algoritmo')
print('b) segundo algoritmo')
op = input('Teclea una opción: ')
if op == 'a':
    n = int(input("Teclea un número: "))
    r=func_factorial(n)
    print(r)
elif op == 'b':
    import factorial2
else:
    print('La opción tecleada es inválida.')