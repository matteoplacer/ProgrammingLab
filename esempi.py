
"""

#esempio 1
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

for elemento in lista:
    if -2 in lista:
        print ('si')


lista = [13, -2, 34, 4, -7, 9]
var=-2
for var in lista:
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

"""

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