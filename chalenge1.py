#!/usr/bin/python3
# Matriz com listas em sequencia
# variaveis auxiliares
# eixo x e y
# classe enumerate

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = 0
b = 0
for x, y in enumerate(matriz):
  #print (y[x])
  a += y[x]
  b += y[-(x+1)]

print (a + b)