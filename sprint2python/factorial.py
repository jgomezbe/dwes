
from tkinter import N


def func_factorial(n):
       
    if n == 1:
        return n
    else:
        return n*func_factorial(n-1)
