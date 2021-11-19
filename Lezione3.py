values = []
my_file=open('shampoo_sales.csv', 'r')
for line in my_file:
    values=my_file.split(',')
    mio_numero=float(values)
    
    

print(my_file.read())
my_file.close()