lista_numeri = [1, 2, 3, 4, 5, 6]

def somma_lista (lista_numeri):
    risultato=0
    for item in lista_numeri:
        risultato=risultato+item
    print('Risultato: {}'.format(risultato))


risultato=somma(lista_numeri)
    