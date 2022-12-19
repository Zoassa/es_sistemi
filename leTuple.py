#le tuple sono come le liste, ma sono immutabili
#si delimitano con le tonde
#punto = (1.5,3.6)
#print(f'La coordinata x del punto è {punto[0]}')
#triangolo  = [(1.5,3.6),(-1.0,0.0),(5.1,4.3)]
#print(f"La coordinata y del secondo vertice è {triangolo[1][1]}")

#dati 3 punti calcolare l'area: 
import math #libreria nativa di python

triangolo  = [(1,2),(3,4),(5,6)] #A B C

area = 1/2 * abs(triangolo[0][0] * triangolo[1][1] + triangolo[0][1] * triangolo[2][0] + triangolo[1][0] * triangolo[2][1] - triangolo[2][0] * triangolo[1][1] - triangolo[2][1] * triangolo[0][0] - triangolo[1][0] * triangolo[0][1])

print(f"Area del triangolo: {area}")