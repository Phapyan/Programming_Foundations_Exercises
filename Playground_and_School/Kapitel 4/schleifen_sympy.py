#Primzahlen mit sympy

import sympy
number = 19

if sympy.isprime(number):
    print(number, "ist Primzahl")
else:
    print(number, "ist keine Primzahl")

