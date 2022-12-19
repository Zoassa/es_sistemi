#fare un programma in python che funga da rubrica telefonica

d = {"Andrea": 33470914123, "Dario": 3490748593, "Favour": 3516887900}

print(d["Andrea"])

nome = input("Inserire un nome: ")
d[nome] = int(input("Inserire il numero di telefono: "))

print(d)