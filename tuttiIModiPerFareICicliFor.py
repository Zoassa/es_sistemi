lista1 = ["a", "b", "c", "d",]
lista2 = [1, 2, 3, 4]

#for su lista1 con C-style --> i primi due sono intercambiabili, meglio il python styile, he il C-style
for indice in range(0, len(lista1)):
    print(lista1[indice], end = "-")
print("")

#for su lista1 con Python style --> 
for elemento in lista1:
    print(elemento, end = "-")
print("")

##for su lista1 con Enumerate --> se devo ciclare sia sull'elemento che sull'indice
for i,e in enumerate(lista1):
    print(e, end = "-")
print("")

#for su tutte e due le liste con Python style (zip)
for a, b in zip(lista1, lista2):
    print(a, b)

#for su tutte e due le liste con C-style (enumerate)

#for su diozionario usando items()

diz = {1:"Mandrile", 2:"Ciao"}
for chiave, valore in diz.items(): 
    print(chiave, valore)

# senza items
for chiave in diz: 
    print(chiave, diz[chiave])