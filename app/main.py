import utils
import read_csv
import chartsProject



def run():

  data = read_csv.read_csv('data.csv') # con esta funcion se lee el archivo y se guarda en una lista de diccionarios

  print('\n','*' * 23, 'CONTINENTES', '*' * 24)
  print(' Africa, Asia, Europe, North America, South America, Oceania','\n','*' * 60,'\n')
  continent = input("Escribe el continente (Type Continent) => ")
  result = utils.filter_by_continent(data,continent) #filtramos la lista a solo los paises del continente elegido
  labels, values = utils.country_poblation_percentage(result) #separamos los paises y porcentajes de poblacion en listas separadas
  chartsProject.generate_pie_charts(labels, values) #generamos el grafico de torta de los paises y su porcentaje de poblacion mundial

if __name__ == '__main__':
  run()