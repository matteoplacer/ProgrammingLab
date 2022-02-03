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
            x=input("Inserire l'inizio dell'intervallo:")
        except Exception as e:
            print("Ho avuto questo errore: {}".format(e))
        if (type(x)!=int):
            print("{} non è un numero intero".format(x))
            fraz,int = modf(x)
			x=(int)
        

        y=input("Inserire la fine dell'intervallo:")

        print("Intervallo: [{},{}]".format(x,y))

        return lista[x-1:y]
        
    
    def _str_(self):
        return 'CSVfile {}'.format(self.name)



File = CSVFile ('shampoo_sales.csv')
Lista = File.get_data()


for line in Lista:
    print(line)



