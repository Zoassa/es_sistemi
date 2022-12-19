operazione = int(input("0 = somma\n1 = sottrazione\n2 = moltiplicazione\n3 = divisione\nInserire un numero: "))
n1 = int(input("Inserire il primo numero: "))
n2 = int(input("Inserire il secondo numero: "))

if(operazione == 0): 
    somma = n1 + n2
    print(f"Somma = {somma}\n")
elif(operazione == 1): 
    if(n1 > n2):
        sottrazione = n1 - n2
        print(f"Sottrazione (primo - secondo) = {sottrazione}\n")
    else: 
        sottrazione = n2 - n1
        print(f"Sottrazione (secondo - primo) = {sottrazione}\n")
elif(operazione == 2): 
    moltiplicazione = n1 * n2
    print(f"Moltiplicazione = {moltiplicazione}\n")
elif(operazione == 3):
    if(n1 == 0 & n2 == 0): 
        print(f"Impossibile svolgere l'operazione di divisione\n")
    else:
        if(n1 == 0): 
            divisione = n1 / n2
            print(f"Divisione = {divisione}\n")
        else: 
            divisione = n2 / n1
            print(f"Divisione = {divisione}\n")

