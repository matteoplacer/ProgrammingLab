from math import modf

class CSVFile ():
    def __init__ (self, name_file):
        self.name=name_file
        if not isinstance (name_file, str):
            raise Exception ('Il file {} non è una stinga'.format(name_file))

    def get_data (self):
        
        lista=[]
        try:
            file = open(self.name, 'r')
        except Exception as e:
            print("Il file non esiste")
            print("Ho avuto questo errore: {}.".format(e))

        for line in file:
            elemento=line.split(',')
            if(elemento[0]!='Date'):
                elemento[1]=elemento[1].strip()
                lista.append(elemento)
        try:
            x=int(input("Inserire l'inizio dell'intervallo:"))
        except Exception as e:
			print("{} non è convertibile in int".format(x))
			print("ho trovato questo errore: {}".format(e))
        if not isinstance(x, int) or (x<0):
            raise Exception("{} non è un numero intero positivo".format(x))
        if (x>len(lista)):
            raise Exception("{} è più grande del numero di linee del file".format(x))

        try:
        	y=input("Inserire la fine dell'intervallo:")
		except Exception as e:
            print("{} non è convertibile in int".format(x))
            print("ho trovato questo errore: {}".format(e))
        if not isinstance(y, int) or y<0:
            raise Exception("{} non è un numero intero positivo".format(y))
        if (y>len(self.name)):
            raise Exception("{} è più grande del numero di linee del file".format(y))
        if (x>y):
            raise Exception(" la fine dell'intervallo {} è minore del suo inizio {}".format(y,x))

        print("Intervallo: [{},{}]".format(x,y))

        return lista[x:y]
        
    
    def _str_(self):
        return 'CSVfile {}'.format(self.name)



File = CSVFile ('shampoo_sales.csv')
Lista = File.get_data()


for line in Lista:
    print(line)



