'''
class CSVFile ():
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
            print('Errore, file non aperto o illeggibile')
        
            return None

        else:
            lista=[]

            file = open(self.name, 'r')


            for line in file:
                elemento=line.split(',')
                if(elemento[0]!='date'):
                    elemento[1]=elemento[1].strip()
                    lista.append(elemento)
            return lista







##########################################
class ExamException(Exception):
    pass


class CSVFile ():
    def __init__ (self, name):
        self.name=name

    def get_data (self):
        lista=[]
        try:
            file = open(self.name, 'r')
        except Exception as e:
            print("Il file non esiste")
            print("Ho avuto questo errore: {}.".format(e))

        for line in file:
            elemento=line.split(',')
            if(elemento[0]!='date'):
                elemento[1]=elemento[1].strip()
                lista.append(elemento)
        return lista


class CSVTimeSeriesFile (CSVFile):
    def __init__(self,name):
        self.name=name

    def get_data(self):
        string_data = super().get_data()
        numerical_data = []

        for string_row in string_data:
            numerical_row = []
            for i,item in enumerate(string_row):
                if i == 0:
                    numerical_row.append(item)  
                else:
                    try:
                        numerical_row.append(float(item))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
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

diff=[]
x=str(input("Inserire il primo anno:"))
y=str(input("Inserire il l'ultimo anno:"))




diff=compute_avg_monthly_difference(time_series, x, y)
for line in diff:
    print(line)

'''

'''
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
            raise ExamException("Il file non esiste")
        
            return None

        string_data=[]

        file = open(self.name, 'r')

        for line in file:
            elemento=line.split(',')
            if(elemento[0]!='date'):
                elemento[1]=elemento[1].strip()
                string_data.append(elemento)
        
        numerical_data = []

        for string_row in string_data:
            numerical_row = []
            for i,item in enumerate(string_row):
                if i == 0:
                    numerical_row.append(item)  
                else:
                    try:
                        numerical_row.append(float(item))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
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

diff=[]
x=str(input("Inserire il primo anno:"))
y=str(input("Inserire il l'ultimo anno:"))




diff=compute_avg_monthly_difference(time_series, x, y)
for line in diff:
    print(line)
'''

print(int(10.0))
