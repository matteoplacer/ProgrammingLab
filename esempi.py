
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

"""

#esempio 5
mylist=['marco', 'giulio', 'matteo', 'fabio']
for i, item in enumerate(mylist):
    print("Posizione {}: {}".format(i, item))

for i in range(3):
    print(i)

for item in mylist: 
    print(item)



#esempio 6


#esempio 7


#esempio 8