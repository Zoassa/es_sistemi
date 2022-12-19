file = open("C:\\Users\\hp\\OneDrive\\Desktop\\CLASSE_QUARTA\\SISTEMI\\matematici.csv", "r")
#lettura file
#questa è una lista che salva le righe al suon interno, non il numero delle righe, ma salva proprio le righe
lista_righe = file.readlines()
print(lista_righe)

#diz_matematici l'ho cambiato in diz

diz = {"id":[], "nome":[]} #gli id sono nuemri, i nomi sono str

for riga in lista_righe[1::]:
    riga_senza_linefeed = riga[:-1]
    print(riga[::-1])
    lista_campi = riga_senza_linefeed.split(",")
    print(lista_campi)
    id = int(lista_campi[0])
    nome = lista_campi[1]
    print(id, nome)
    diz["id"].append(id)
    diz["nome"].append(nome[1:])

print(diz)
#per avere i nomi: 
print(diz["nome"])

file.close()



#programma con funzioni: 

def leggi_file(nome_file):
    file = open("C:\\Users\\hp\\OneDrive\\Desktop\\CLASSE_QUARTA\\SISTEMI\\matematici.csv", "r")
    lista_righe = file.readlines()
    file.close()

diz = {"id":[], "nome":[]} #gli id sono nuemri, i nomi sono str

for riga in lista_righe[1::]:
    riga_senza_linefeed = riga[:-1]
    print(riga[::-1])
    lista_campi = riga_senza_linefeed.split(",")
    print(lista_campi)
    id = int(lista_campi[0])
    nome = lista_campi[1]
    print(id, nome)
    diz["id"].append(id)
    diz["nome"].append(nome[1:])

print(diz)
#per avere i nomi: 
print(diz["nome"])


#main in python: 
#def main():
    #scrivo le cose

#main() --> richiamo il main 

def main():
    file = open("nomeFile.csv", "r")
    righe = file.readlines()
    file.close()
    diz = {"id":[], "nome":[]}
    for riga in righe[1:]:
        #print(riga)
        campi_riga = riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1])

        

    print(diz)


#funzione di ricerca: 
def leggi_file():
    file = open("nomeFile.csv", "r")
    righe = file.readlines()
    file.close()
    diz = {"id":[], "nome":[]}
    for riga in righe[1:]:
        #print(riga)
        campi_riga = riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1])

        

    print(diz)

def nome_id(id, diz): 
    listaId = diz("id")
    listaNomi = diz("nome")
    #print(listaNomi)
    #i = id, n = nome
    for i, n in zip(listaId, listaNomi): #si può fare solo se le liste sono lunghe uguali
        #print(i, n)
        if i == id: 
            return n


def main(): 
    diz = leggi_file()
    id = 2
    nome = nome_id(id, diz)
    print(nome)


