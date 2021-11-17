#io
lista_numeri = [14, 5, 9, 1, 7, 2]

def somma_lista (lista_numeri):
    risultato=0
    for x in lista_numeri:
        risultato=risultato+x
    print('Risultato: {}'.format(risultato))

risultato=somma_lista (lista_numeri)

#davide
def myfun(my_list):
    s=0
    for item in my_list:
        s=s+item
    return s;
my_list=[1,2,3,4]
s=myfun(my_list)
print("la somma è: {}".format(s)
#print("la somma è: {}".format(myfun(my_list)))