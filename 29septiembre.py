# -*- coding: utf-8 -*-
"""29Septiembre

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1215A3-dq--isC90K-K1qoevW5qXPXGkB
"""

Edad = 21

print(Edad)
colores = ('rojo','azul','verde','morado','violeta')
print(colores)

colores[3]
print(colores[3])

# Solo mostrar la 'ra' de morado ?
print(colores[3][2:4])
nombre = "Javier"
print(nombre[0])
print(nombre[0:3:1])

"""# For en Python 3

     2 variantes
     1. j in range (ini,tope,incr)
     2.in (iterador)
"""

for j in range(0,5,1):
  print(colores[j])

for j in range(0,len(nombre),1):
  print(nombre[j])

"""## ¿Qué es MarkDown?

MarkDown es un lenguaje de marcado para comentar código. El objetivo es simplificar la escritura de HTML.
___
**Negritas**
____
***
MasMMas información
"""