n1 = int(input("Inserire un numero: "))

if(n1 % 2 == 0): 
    print(f"Il numero è divisibile per 2\n")
elif(n1 % 3 == 0): 
    print(f"Il numero è divisibile per 3\n")
else: 
    print(f"Il numero è divisibile per 5\n")