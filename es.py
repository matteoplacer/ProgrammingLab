

class CSVFile ():
    def __init__ (self, name_file):
        self.name=name_file

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
        return lista


class CSVFileNumerico ():
    def __init__ (self, name_file):
        self.name=name_file

    def get_data2 (self):
        lista=[]
        file = open(self.name, 'r')
        for line in file:
            elemento=line.split(',')
            if(elemento[1]!='Sales\n'):
                elemento[1]=elemento[1].strip()
                try:
                    elemento[1]=float(elemento[1])
                except Exception as E:
                    print("Non posso convertire {} a valore numerico".format(elemento[1]))
                    print("Ho avuto questo errore: {}.".format(E))
                    print("Di default verrà inserito none")
                    elemento[1]=None
                lista.append(elemento[1])
        return lista


File = CSVFile ('shampoo_sales.csv')
Lista = File.get_data()
File2 = CSVFileNumerico ('shampoo_sales_lezione5.csv')
Lista2 = File2.get_data2()

for line in Lista2:
    print(line)
