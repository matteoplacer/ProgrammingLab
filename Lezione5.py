class CSVfile():

    def __init__(self,file_name):
        self.name=file_name
        
    def get_data(self):
        try:
            openedfile=open(self,'r')
        except Exception as e:
            print ("il file in questione non esiste")
            print ("ho avuto questo errore:{}".format(e))  
        data=[]
        for line in openedfile:
            elements=line.split(',')
            if (elements[0]!='Date'):
                data.append(elements)
        return data
    def _str_(self):
        return 'CSVfile {}'.format(self.name)

class CSVfilenumerico:

    def __init__(self,file_name):
        self.name=file_name

    def change_type(self):
        openedfile=open(self.name, 'r')
        sales=[]
        for line in openedfile:
            elements=line.split(',')
            if(elements[1]!='Sales\n'):
                try:
                    my_num=float(elements[1])
                except Exception as e:
                    print("non è convertibile in float {}".format(elements[1]))
                    print("ho trovato questo errore: {}".format(e))
                    my_num='\n'
                sales.append(my_num)
        return sales

my_file=CSVfile('shampoo_sales.csv')
my_file2=CSVfilenumerico('shampoo_sales_lezione5.csv')
sales=my_file2.change_type()
for item in sales:
    print (item)


#==============================
#  Classe per file CSV
#==============================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self):
        
        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
    
            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:
                
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')
                
                # Posso anche pulire il carattere di newline 
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()
                
                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.
    
                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                        
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data



#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        
        # Chiamo la get_data del genitore 
        string_data = super().get_data()
        
        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []
        
        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:
            
            # Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []
            
            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i,element in enumerate(string_row):
                
                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)
                    
                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data

   

#==============================
#  Corpo del programma
#==============================



mio_file_numerico = NumericalCSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file_numerico.name))
print('Dati contenuti nel file: "{}"'.format(mio_file_numerico.get_data()))
