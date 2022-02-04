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
        
        x=int(input("Inserire l'inizio dell'intervallo: "))
        y=int(input("Inserire la fine dell'intervallo: "))
        
        x=abs(x)
        y=abs(y)
        if(x>y):
            t=y
            y=x
            x=t

        if x>len(lista):
            raise Exception("Il numero {} è maggiore della lunghezza della lista".format(x))

        if y>len(lista):
            raise Exception("Il numero {} è maggiore della lunghezza della lista".format(y))

        print("Intervallo: [{},{}]".format(x,y))

        return lista[x:y]
        

    def _str_(self):
        return 'CSVfile {}'.format(self.name)


File = CSVFile ('shampoo_sales.csv')
Lista = File.get_data()

for line in Lista:
    print(line)




"""
class CSVfile():

    def __init__(self,file_name):
        self.name=file_name
        if not isinstance(file_name, str):
            raise Exception ('il file non è una stringa')
            
    def get_data(self):
        data=[]
        #inserisco manualmente l'inizio dell'intervallo e sanitizzo òe possibili eccezioni
        try:
            x=int(input("inserisci l'inizio dell'intervallo:"))
        except Exception as e:
            print("{} non è convertibile in int".format(x))
            print("ho trovato questo errore: {}".format(e))
        if not isinstance(x, int) or (x<0):
            raise Exception("{} non è un numero intero positivo".format(x))
        if (x>len(self.name)):
            raise Exception("{} è più grande del numero di linee del file".format(x))

        #inserisco manualmente la fine dell'intervallo e sanitizzo òe possibili eccezioni
        try:
            y=int(input("inserisci l'inizio dell'intervallo:"))
        except Exception as e:
            print("{} non è convertibile in int".format(x))
            print("ho trovato questo errore: {}".format(e))
        if not isinstance(y, int) or y<0:
            raise Exception("{} non è un numero intero positivo".format(y))
        if (y>len(self.name)):
            raise Exception("{} è più grande del numero di linee del file".format(y))
        if (x>y):
            raise Exception(" la fine dell'intervallo {} è minore del suo inizio {}".format(y,x))
        openedfile=open(self.name,'r')
        for line in openedfile:
            elements=line.split(',')
            if (elements[0]!='Date'):
                try:
                    data.append(elements[0])
                except:
                    raise Exception ("non è stato possibile convertire il file in una lista")
        return data[x:y]
    def _str_(self):
        return 'CSVfile {}'.format(self.name)

my_file=CSVfile('shampoo_sales.csv')
dataM=my_file.get_data()
for line in dataM:
    print (line)
"""