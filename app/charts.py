import matplotlib.pyplot as plt
import read_csv

def generate_bar_chart(labels, values):

  fig, ax = plt.subplots() #este metodo crea una parcela para el grafico
  ax.bar(labels, values) #metodo para crear el grafico de barras, se le pasan los encabezados como argumentos
  plt.savefig('bar.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels) #metodo para crear graficas circulares
  ax.axis('equal') #metodo para centrar la grafica
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__': # Para ejecutar como Script
  data = read_csv('./app/data.csv')
  labels = ['a', 'b', 'c']
  values = [10, 30, 60]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)