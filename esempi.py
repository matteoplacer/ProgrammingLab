
"""

#esempio 1 (LEZIONE 2)
lista = [13, -2, 34, 4, -7, 9]

for elemento in lista:
    if elemento > 0:
        print (elemento)

print('Lista={}'.format(lista))

#esempio 2
stringa='Ciao, sono Matteo. Vivo a Trieste. Tu come ti chiami e dove vivi ?'
#print('{}'.format(stringa[19:-8]))
stringa2=stringa[19:-8]
print('{}'.format(stringa2))

#esempio 3
lista = [13, -2, 34, 4, -7, 9]

if -2 in lista:
        print ('si')


lista = [13, -2, 34, 4, -7, 9]
var=-2
if var in lista:
    print ('si')


#esempio 4
my_var=1.8
your_var=0.9
if (my_var > your_var):
    print("My var is bigger than yours")
    if (my_var-your_var) <= 1:
        print("...but not so much")
    elif (my_var-your_var) <= 5:
        print("...quite a bit")
    else: 
         print("...a lot")
else:
    print('Your var is bigger than my var')
    if (your_var-my_var) <= 1:
        print("...but not so much")
    elif (your_var-my_var) <= 5:
        print("...quite a bit")
    else: 
         print("...a lot")


#esempio 5
mylist=['marco', 'giulio', 'matteo', 'fabio']
for i, item in enumerate(mylist):
    print("Posizione {}: {}".format(i, item))

for i in range(3):
    print(i)

for item in mylist: 
    print(item)


#esempio 6
var=-7
x=2
y=3
var=abs(var)
print('{}'.format(var))
#print('{}'.format(abs(var)))
print('potenza: {}'.format(pow(x,y)))

lista = [13, -2, 34, 4, -7, 9]
somma=sum(lista)
print('somma: {}'.format(somma))
#print('somma: {}'.format(sum(lista)))
print('max: {}'.format(max(lista)))
print('min: {}'.format(min(lista)))
print('lunghezza: {}'.format(len(lista)))


#esempio 7
import math
def funzione (x, y):
    print('somma: {}'.format(x+y))
    print('sottrazione: {}'.format(x-y))
    print('moltiplicazione: {}'.format(x*y))
    print('divisione: {}'.format(x/y))
    print('potenza: {}'.format(pow(x,y)))
    print('minimo: {}'.format(min(x,y)))
    print('massimo: {}'.format(max(x,y)))
    print('valore assoluto x: {}'.format(abs(x)))
    print('valore assoluto y: {}'.format(abs(y)))
    print('radice quadrata x: {}'.format(math.sqrt(x)))
    print('radice quadrata y: {}'.format(math.sqrt(y)))

x=5
y=8
funzione (x,y)


#esempio 8
my_list = ["marco", "irene", "paolo"]
if "marco" in my_list:
    print("Ho trovato marco!")

lista = [13, -2, 34, 4, -7, 9]
var=4
if 4 in lista:
    print ('Si!')


#esempio 9 (esercizio lezione 2)
def somma_lista (lista):
    somma=0
    for elemento in lista:
        somma=somma+elemento
    return somma

lista=[3,9,6,4,2,5]
print('La somma degli elementi nella lista è: {}'.format(somma_lista(lista)))


#esempio 10 (LEZIONE 3)
file=open('shampoo_sales.csv', 'r')
#print(file.read())
print(file.read()[0:50])
file.close()


#esempio 11
# Apro il file
file=open('shampoo_sales.csv', 'r')
# Leggo il contenuto
my_file_contents = file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)
# Chiudo il file
file.close()


#esempio 12
file = open('shampoo_sales.csv', 'r')
print(file.readline())
print(file.readline())
file.close()


#esempio 13
file = open('shampoo_sales.csv', 'r')
for line in file:
    print(line)
file.close()


#esempio 14 
file = open('shampoo_sales.csv', 'r')
for i in range(5):
    print(file.readline())
file.close()

i=0
file = open('shampoo_sales.csv', 'r')
for line in file:
    if(i>4): break;
    print(line)
    i=i+1
file.close()

file = open('shampoo_sales.csv', 'r')
for i, line in enumerate(file):
    if(i>4): break;
    print(line)
file.close()


#esempio 15
stringa='ciao, come va?'
separazione=stringa.split(',')
print('{}'.format(separazione))

stringa='5.5'
numero=float(stringa)
print('{}'.format(numero))

lista=[1,2,3]
lista.append(4)
print('{}'.format(lista))


#esempio 16
# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
file = open('shampoo_sales.csv', 'r')
for line in file:
    # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
    #print('{}'.format(elements))
    # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
        # Setto la data e il valore
        date = elements[0]
        value = elements[1]
        # Aggiungo alla lista dei valori questo valore
        values.append(float(value))
#somma=sum(values)
file.close()
print('{}'.format(values))
#print('{}'.format(somma))

"""

#esempio 17 (esercizio lezione 3)
def somma_lista (file):
    valori=[]
    for line in file:
        elemento=line.split(',')
        if(elemento[0]!='Date'):
            valore=elemento[1]
            valori.append(float(valore))
    return(sum(valori))

file = open('shampoo_sales.csv', 'r')
print('{}'.format(somma_lista(file)))
file.close()   


#esempio 18 (LEZIONE 4)




