'''
non esiste privato o pubblico, tutto è di norma pubblico
'''

class IPadress():
    #costruttore --> IN TUTTI I PROGRAMMI HA LO STESSO NOME, INDIPENDENTEMENTE DAL NOME DELLA CLASSE
    #il SELF ci va SEMPRE
    #tutti i metodi di una classe in python sono sempre: metodo(self, ...):
    def __init__(self, ip_stringa):
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin = None
        

    def dec2bin(self):
        pass #fare di compito

    def toList(self):
        lista_stringhe = self.ip_notazione_dec.split(".")
        return [int(gruppo) for gruppo in lista_stringhe]
    
    def binn(ip):
        return (bin(ip))

def main():
    indirizzoIP = IPadress("192.168.0.123")
    print(indirizzoIP.ip_notazione_dec)
    print(indirizzoIP.toList)
    #num = 15
    #print(bin(num))
    #print(binn(ip))

if __name__ == '__main__':
    main()

'''
fare un metodo che converta in binario l'indirizzo in decimale senza return
'''
