#definisco la mia classe per le eccezioni 
class ExamException(Exception):
    pass


class CSVTimeSeriesFile ():
    def __init__ (self, name):
        self.name=name

        #controllo che il file esista e sia leggibile
        try:
            file = open(self.name, 'r')
            file.readline()
        except:
            raise ExamException("Errore in apertura del file, il file non esiste o non è leggibile")
    
    def get_data (self):


        string_data=[]

        file = open(self.name, 'r')

        #creo una lista con le date corrette per poi controllare se quelle del file sono corrette
        control_data=[]
        for i in range(1949, 1961, 1):
            x=str(i)
            for k in range(1, 13, 1):
                if(k<10):
                    control_data.append(x+'-0'+str(k))
                else:
                    control_data.append(x+'-'+str(k))
            
        #creo una lista di liste dagli elementi del file separandoli dove c'è la virgola, inoltre gli elementi all'interno delle liste sono tutti in formato stringa
        for line in file:
            elemento=line.split(',')
            if(elemento[0]!='date'):
                elemento[1]=elemento[1].strip()
                string_data.append(elemento)

        #creo una lista con tutti gli anni e i mesi in formato stringa per poi confrontarla con la mia lista control_data
        anni_mesi=[]
        for item in string_data:
            anni_mesi.append(item[0])

        #controllo se gli anni del mio file (copiati nella lista anni_mesi), sono uguali agli anni "giusti" inseriti nella lista control_data
        for item in anni_mesi:
            if(item not in control_data):
                raise ExamException("Errore, la data {} non è valida.".format(item))
            if(anni_mesi.count(item)>1):
                raise ExamException("Errore, la data {} si ripete.".format(item))
        
        numerical_data = []

        #trasformo la mia lista di liste in formato stringa trasformando il valore dei passeggeri da stringa a float e faccio anche dei controlli sulle stringhe da convertire
        for string_row in string_data:
            numerical_row = []
            for i,item in enumerate(string_row):
                if i == 0:
                    numerical_row.append(item) 
                else:
                    #controllo se manca un valore per un mese 
                    if item=='':
                        print("Errore, il valore riguardante la data {} non è presente.".format(string_row[0]))
                    else:
                        #controllo che il valore dei passeggeri sia una stringa convertibile in float
                        try:
                            numerical_row.append(float(item))
                        except:
                            print("Errore in conversione del valore '{}' (data: {})".format((item),string_row[0]))
                        else:
                            #controllo che il valore dei passeggeri è uguale a 0
                            if float(item) == 0:
                                print("Errore, il valore {} è nullo (data: {})".format(float(item), string_row[0]))
                                numerical_row.remove(float(item))
                            #controllo che il valore cei passeggeri sia positivo
                            if float(item) < 0:
                                print("Errore, il valore {} è negativo (data: {})".format(float(item),string_row[0]))
                                numerical_row.remove(float(item))

            numerical_data.append(numerical_row)
        return numerical_data


def compute_avg_monthly_difference (time_series, first_year, last_year):

    values=[]
    difference=[]
    x=0
    h=0
    z=0

    #calcolo la differenza tra i due anni che poi mi servirà per calcolare la differenza media del numero di passeggeri al mese
    l=(int(last_year)-int(first_year))
    
    #aggiungo alle mie due stringhe di anni i relativi mesi per poi confrontarli con quelli del file
    first_year=str(first_year)+'-01'
    last_year=str(last_year)+'-12'

    #creo una lista con i valori dei passeggeri, che corrispondono agli anni dell'intervallo di tempo 
    for item in time_series:
        if(first_year==item[0]):
            for elem in time_series:
                z=z+1
                if z>h:
                    if len(elem)<=1:
                        values.append(0)
                    else:
                        values.append(elem[1])
                if(last_year==elem[0]):
                    break
        h=h+1

    #calcolo e aggiungo i valori delle differenze medie alla mia lista
    #azzero il contatore h (usato precedentemente) per poterlo riutilizzare per controllare e verificare i valori dei numeri di passeggeri
    for i in range (0,12,1):
        h=0
        #calcolo quali valori relativi a ogni mese sono uguali a 0, quindi dove ho dei dati mancanti
        for z in range(i, (l*12)+12, 12):
            if(values[z] != 0): 
                h=h+1
        for k in range (i, l*12, 12):
            #analizzo i casi dove ho dei dati mancanti
            #(1° caso) lunghezza dell'intervallo uguale a 1 e mancano uno e entrambi i dati relativi al mese
            if(l==1 and h<2):
                difference.append(0)
                break
            #(2° caso) ho intervalli di tempo di più di due anni e ho più di un dato allora posso calcolare la mia differenza media per il mese
            elif h>1:
                x+=(values[k+12]-values[k])
            #altrimenti se ho meno di un dato non posso calcolare la mia differenza media per il mese in questione
            else: 
                difference.append(0)
                break
        #nel caso non sono riuscito a calcolare la differenza media per dei mesi allora salto questo passaggio
        if(h>1): 
            if(l!=1 or (values[k]!=0 and values[k+12]!=0)):
                difference.append(x/l)
        #riazzero il contatore h e la x per ripetere tutto il procedimento per un altro mese
        x=0 
        h=0

    return difference



time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

'''
print('Nome del file: "{}"'.format(time_series_file.name))
print('Dati contenuti nel file:')

for line in time_series:
    print(line)
#print('Dati contenuti nel file: \n"{}"'.format(time_series))
'''

#creo una lista con tutti gli anni appartenenti al file
string_years=[]

for item in time_series:
    string_years.append(item[0])

#chiedo in input l'intervallo di tempo
x=str(input("Inserire il primo anno:"))
y=str(input("Inserire il l'ultimo anno:"))

#controllo che i valori inseriti siano un numero
try:
    int(x)
except:
    raise ExamException("Errore!  L'estremo inferiore dell'intervallo di tempo non è un anno")

try:
    int(x)
except:
    raise ExamException("Errore! L'estremo superiore dell'intervallo di tempo non è un anno")

#controllo che l'intervallo abbia senso 
if int(y) < int(x):
    raise ExamException("Errore! L'estremo inferiore dell'intervallo di tempo è maggiore dell'estremo superiore dello stesso intervallo")

if int(y) == int(x):
    raise ExamException("Errore! I due estremi dell'intervallo di tempo sono uguali")

f_y=x+'-01'
l_y=y+'-12'

#controllo che il mio intervallo appartenga agli anni contenuti nel file
if f_y not in string_years:
    raise ExamException("L'estremo inferiore dell'intervallo di tempo non è presente nel file")

if l_y not in string_years:
    raise ExamException("L'estremo inferiore dell'intervallo di tempo non è presente nel file")

#creo la lista dove salverò il miei risultati
differenza_media_mesi=[]

differenza_media_mesi=compute_avg_monthly_difference(time_series, x, y)
print("La differenza media del numero di passeggeri mensile tra il {} e il {} è:".format(x,y))

#stampo la mia lista con i valori delle differenze medie del numero di passeggeri tra i due anni inseriti dall'utente per ogni mese aggiungendo il numero del mese per semplificare la lettura
i=0
for line in differenza_media_mesi:
    i=i+1
    print("{}: {}".format(i, line))
