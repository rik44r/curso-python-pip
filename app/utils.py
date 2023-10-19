def filter_by_continent (data, continent):
  
  continent_filter = list(filter(lambda item: item['Continent'] == continent,data)) #filtro solos los paises del continente elegido
  
  return continent_filter

def country_poblation_percentage(continent_filter):
  
  country = []  #lista para guardar los paises
  percentage = []  #lista para guardar el porcentaje de poblacion
  for r in continent_filter:  #iteracion para guardar solo los paises y porcentajes en sus listas correspondientes
    country.append (r['Country/Territory'])
    percentage.append (r['World Population Percentage'])
  return country , percentage