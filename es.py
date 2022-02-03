

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



