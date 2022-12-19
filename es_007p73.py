lista = [4,8,6,3,4,5,7]

max, min = lista[0]

def maxMin(m1, m2):
    for k in lista: 
        if(lista[k] > max):
            max = lista[k]
        
        if(lista[k] < min):
            min = lista[k]

    return max, min

print(max)
print(min)

