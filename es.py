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
            x=int(input("Inserire l'inizio dell'intervallo: "))
        except Exception as e:
            print("Errore generico: {}".format(e))
            print("La variabile x di default assumerà valore 0")
            x=0
        if x<0 or x>len(lista):
            raise Exception("Il numero inserito è negativo o maggiore della lunghezza della lista")

        try:
            y=int(input("Inserire la fine dell'intervallo: "))
        except Exception as e:
            print("Errore generico: {}".format(e))
            print("La variabile y di default assumerà valore pari alla lunghezza della lista")
            y=len(lista)
        if y<0 or y>len(lista):
            raise Exception("Il numero inserito è negativo o maggiore della lunghezza della lista")
        if x>y:
            raise Exception("La fine dell'intervallo è minore del suo inizio")     

        print("Intervallo: [{},{}]".format(x,y))

        return lista[x:y]
        
    
    def _str_(self):
        return 'CSVfile {}'.format(self.name)



File = CSVFile ('shampoo_sales.csv')
Lista = File.get_data()


for line in Lista:
    print(line)



