import csv #modulo nativo de python para leer archivos csv

def read_csv (path):
  with open ( path , 'r') as csvfile: #leer el archivo data.csv y guardarlo en csvfile
    reader = csv.reader(csvfile, delimiter=',') #leemos los datos de csvfile y le decimos que los datos estan separados con ','(delimitador)
    header = next(reader) #como reader es un iterable podemos iterar la primera fila con next y guardarlo en header
    #print(header)
    data = [] #Lista para guardar luego el diccionario
    for row in reader:
      iterable = zip (header, row) #con el zip vamos a crear la union del header(keys) con row(values), esto va convertirlo en un array de tuplas en pares.
      country_dict = {key: value for key, value in iterable} #convertimos el array de tuplas en diccionario con dictionary comprehension
      data.append(country_dict) #agregamos el dictionario a la lista data[]
      
    return data

if __name__ == '__main__': #funcion para que el programa tambien pueda correr desde la terminal como un script
  data = read_csv('./app/data.csv') #como tenemos un return en la funcion del programa guardamos eso en data.
  print (data)
      