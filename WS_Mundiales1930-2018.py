#Extraccion de datos con BeutifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup
 

years = [1930, 1934, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2010, 2014,
         2018, 2022]

def get_matches(years):
    web = f'https://en.wikipedia.org/wiki/{years}_FIFA_World_Cup'
    #Usamos 'requests' para obtener una respuesta de la página web
    response = requests.get(web)
    content = response.text
    #Usamos BeautifulSoup para leer de mejor manera la información que obtuvimos como respuesta
    soup = BeautifulSoup(content, 'lxml')

    #Metodo 'find_all' para inspeccionar la página
    #Notamos que todos los partidos vienen en la clase 'fooballbox'
    matches = soup.find_all('div',class_='footballbox')
    #Método 'find_all' nos devuelve una lista
    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())

    #Creamos un diccionario para luego convertirlo en un DataFrame
    dict_football = {'Home': home,'Score': score,'Away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['Year'] = years
    return df_football

#Bucle For para obtener la data de todos los mundiales
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('Datasets/Fifa_WorldCup_Historical_Data.csv', index=False)