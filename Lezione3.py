
#Dennis (senza funzione)

values = []

my_file = open('shampoo_sales.csv', 'r')

for line in my_file:
    elements = line.split(',') 
    if elements[0] != 'Date':
     date = elements[0]
     value = elements[1]
     values.append(float(value))

sum(values)

print(sum(values))
my_file.close()


#Manu (con funzione)

#Definisco la mia funzione
def somma_valori_file(my_file):

    #Inizializzo una lista vuota per salvare i valori
    values=[]
    
    #Scrivo un ciclo for
    for line in my_file:

        #Divido la stringa (faccio lo split di ogni riga sulla virgola)
        elements=line.split(",")

        #Se NON sto processando l'intestazione e le date
        if (elements[0]!="Date"): 

            #Setto il valore
            numero=elements[1]           

            #Aggiungo alla lista dei valori questo valore      
            values.append(float(numero))
    
    #Chiudo il file 
    my_file.close()

    #Ritorno la somma della lista
    return(sum(values))

#Apro il file 
my_file_shampoo=open("shampoo_sales.csv","r")

#Mostro il risultato della somma
print(somma_valori_file(my_file_shampoo))