import matplotlib.pyplot as plt

def generate_pie_charts(labels, values):
  #print (labels , values)
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  #plt.legend(title = "Paises:")
  plt.savefig('pie2.png')
  plt.close()


if __name__ == '__main__':
  #data = read_csv('./app/data.csv')
  labels = ['a', 'b', 'c']
  values = [10, 30, 60]
  #generate_bar_chart(labels, values)
  generate_pie_charts(labels, values)
