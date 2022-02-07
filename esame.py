class ExamException(Exception):
    pass


class CSVTimeSeriesFile ():
    def __init__ (self, name):
        self.name=name

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

    def get_data (self):

        if not self.can_read:
            raise ExamException("Il file non esiste o non è leggibile.")
        
            return None

        string_data=[]

        file = open(self.name, 'r')

        control_data=[]
        for i in range(1949, 1961, 1):
            x=str(i)
            for k in range(1, 13, 1):
                if(k<10):
                    control_data.append(x+'-0'+str(k))
                else:
                    control_data.append(x+'-'+str(k))
            

        for line in file:
            elemento=line.split(',')
            if(elemento[0]!='date'):
                elemento[1]=elemento[1].strip()
                string_data.append(elemento)


        anni_mesi=[]
        for item in string_data:
            anni_mesi.append(item[0])

        for item in anni_mesi:
            if(item not in control_data):
                raise ExamException("Errore, la data {} non è valida.".format(item))
            if(anni_mesi.count(item)>1):
                raise ExamException("Errore, la data {} si ripete.".format(item))
        

        numerical_data = []

        for string_row in string_data:
            numerical_row = []
            for i,item in enumerate(string_row):
                if i == 0:
                    numerical_row.append(item) 
                else:
                    if item=='':
                        print("Errore, il valore riguardante la data {} non è presente.".format(string_row[0]))
                    else:
                        try:
                            numerical_row.append(float(item))
                        except:
                            print("Errore in conversione del valore {} (data: {})".format((item),string_row[0]))
                        else:
                            if float(item) == 0:
                                print("Errore, il valore {} è nullo (data: {})".format(float(item), string_row[0]))
                                numerical_row.remove(float(item))
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

    l=(int(last_year)-int(first_year))
    
    first_year=str(first_year)+'-01'
    last_year=str(last_year)+'-12'

    for item in time_series:
        if(first_year==item[0]):
            for elem in time_series:
                z=z+1
                if z>h:
                    values.append(elem[1])
                if(last_year==elem[0]):
                    break
        h=h+1

    
    for i in range (0,12,1):
        for k in range (i, l*12, 12):
            x+=(values[k+12]-values[k])
        difference.append(x/l)
        x=0 

    return difference




time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

print('Nome del file: "{}"'.format(time_series_file.name))
print('Dati contenuti nel file:')
for line in time_series:
    print(line)
#print('Dati contenuti nel file: \n"{}"'.format(time_series))

numerical_years=[]

for item in time_series:
    numerical_years.append(item[0])


'''
tutte_le_date=[]
for item in time_series:
    tutte_le_date.append(item[0])
print(tutte_le_date)
'''


diff=[]
x=str(input("Inserire il primo anno:"))
y=str(input("Inserire il l'ultimo anno:"))

try:
    int(x)
except:
    raise ExamException("Errore!  L'estremo inferiore dell'intervallo di tempo non è un anno")

try:
    int(x)
except:
    raise ExamException("Errore! L'estremo superiore dell'intervallo di tempo non è un anno")


if int(y) < int(x):
    raise ExamException("Errore! L'estremo inferiore dell'intervallo di tempo è maggiore dell'estremo superiore dello stesso intervallo")

f_y=x+'-01'
l_y=y+'-12'

if f_y not in numerical_years:
    raise ExamException("L'estremo inferiore dell'intervallo di tempo non è presente nel file")

if l_y not in numerical_years:
    raise ExamException("L'estremo inferiore dell'intervallo di tempo non è presente nel file")

diff=compute_avg_monthly_difference(time_series, x, y)
for line in diff:
    print(line)
